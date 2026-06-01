# Flyway Migration Patterns for Domain Events

## Domain Event Store Table

```sql
-- V1__create_domain_event_store.sql
CREATE TABLE domain_event_store (
    id              VARCHAR(36) PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_version   INT NOT NULL DEFAULT 1,
    event_data      JSONB NOT NULL,
    metadata        JSONB,
    occurred_at     TIMESTAMPTZ NOT NULL,
    processed       BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_event_aggregate_id ON domain_event_store(aggregate_id);
CREATE INDEX idx_event_type ON domain_event_store(event_type);
CREATE INDEX idx_event_occurred_at ON domain_event_store(occurred_at);
CREATE INDEX idx_event_processed ON domain_event_store(processed)
    WHERE processed = FALSE;
```

## Outbox Pattern Table

```sql
-- V2__create_outbox_table.sql
CREATE TABLE outbox_message (
    id              VARCHAR(36) PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    payload         JSONB NOT NULL,
    trace_id        VARCHAR(64),
    destination     VARCHAR(255),
    status          VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    retry_count     INT NOT NULL DEFAULT 0,
    max_retries     INT NOT NULL DEFAULT 3,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_attempt_at TIMESTAMPTZ,
    processed_at    TIMESTAMPTZ
);

CREATE INDEX idx_outbox_status ON outbox_message(status)
    WHERE status IN ('PENDING', 'RETRYING');
CREATE INDEX idx_outbox_created ON outbox_message(created_at);
```

## Event Sourcing Snapshots

```sql
-- V3__create_event_snapshot_table.sql
CREATE TABLE event_snapshot (
    aggregate_id    VARCHAR(36) PRIMARY KEY,
    aggregate_type  VARCHAR(100) NOT NULL,
    version         INT NOT NULL,
    state           JSONB NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Projection Table for CQRS Read Model

```sql
-- V4__create_order_read_model.sql
CREATE TABLE order_read_model (
    id              VARCHAR(36) PRIMARY KEY,
    customer_id     VARCHAR(36) NOT NULL,
    customer_name   VARCHAR(100),
    status          VARCHAR(20) NOT NULL,
    total_amount    DECIMAL(12,2) NOT NULL,
    currency        VARCHAR(3) NOT NULL DEFAULT 'CNY',
    item_count      INT NOT NULL DEFAULT 0,
    paid_at         TIMESTAMPTZ,
    shipped_at      TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    version         INT NOT NULL DEFAULT 1
);

CREATE INDEX idx_read_model_customer ON order_read_model(customer_id);
CREATE INDEX idx_read_model_status ON order_read_model(status);
```

## Idempotency Table

```sql
-- V5__create_idempotency_table.sql
CREATE TABLE idempotency_key (
    id              VARCHAR(64) PRIMARY KEY,
    consumer        VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_id        VARCHAR(36) NOT NULL,
    response        JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(consumer, event_type, event_id)
);

-- Auto-expire old entries (TTL equivalent)
CREATE INDEX idx_idempotency_created ON idempotency_key(created_at);
```

## Migration Script for Event-Enabling Existing Tables

```sql
-- V6__add_domain_events_to_existing_tables.sql

-- 1. Add event tracking columns to existing domain tables
ALTER TABLE orders ADD COLUMN IF NOT EXISTS last_event_type VARCHAR(200);
ALTER TABLE orders ADD COLUMN IF NOT EXISTS last_event_at TIMESTAMPTZ;
ALTER TABLE orders ADD COLUMN IF NOT EXISTS event_version INT DEFAULT 0;

-- 2. Create trigger function for event tracking
CREATE OR REPLACE FUNCTION track_domain_event()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_event_at = NOW();
    NEW.event_version = OLD.event_version + 1;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 3. Apply trigger
CREATE TRIGGER trg_order_event_tracking
    BEFORE UPDATE ON orders
    FOR EACH ROW
    EXECUTE FUNCTION track_domain_event();
```

## Liquibase Equivalents

```xml
<changeSet id="1" author="devops">
    <createTable tableName="domain_event_store">
        <column name="id" type="VARCHAR(36)">
            <constraints primaryKey="true"/>
        </column>
        <column name="aggregate_id" type="VARCHAR(36)">
            <constraints nullable="false"/>
        </column>
        <column name="event_type" type="VARCHAR(200)">
            <constraints nullable="false"/>
        </column>
        <column name="event_data" type="JSONB"/>
        <column name="occurred_at" type="TIMESTAMPTZ">
            <constraints nullable="false"/>
        </column>
    </createTable>
    <createIndex tableName="domain_event_store"
                 indexName="idx_aggregate_id">
        <column name="aggregate_id"/>
    </createIndex>
</changeSet>
```
