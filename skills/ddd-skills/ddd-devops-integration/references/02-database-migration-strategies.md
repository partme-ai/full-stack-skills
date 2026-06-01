# Database Migration Strategies for DDD

## Migration Strategy Decision Matrix

| DDD Scenario | Strategy | Tool | Key Considerations |
|-------------|----------|------|--------------------|
| Layered/Onion (single DB) | Sequential migrations | Flyway/Liquibase | One migration script per schema change |
| CQRS L2 (read/write separation) | Dual migration tracks | Flyway + custom scripts | Handle replication lag, eventual consistency |
| Event Sourcing | Schema-less event store | Axon/EventStoreDB | Append-only, no migration for event data |
| Microservices + DDD | Per bounded context independent DB | Per-service Flyway | Schema-per-service, avoid cross-service joins |
| Outbox pattern | Outbox + event tables as migration seeds | Flyway | Outbox table schema must be included in migrations |

## Outbox Pattern Migration

```sql
-- V1__create_outbox_for_domain_events.sql
CREATE TABLE outbox (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_id VARCHAR(36) NOT NULL,
    aggregate_type VARCHAR(100) NOT NULL,
    event_type VARCHAR(200) NOT NULL,
    event_id VARCHAR(36) NOT NULL,
    payload JSONB NOT NULL,
    trace_id VARCHAR(64),
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    processed_at TIMESTAMPTZ,
    UNIQUE(event_type, event_id)
);

CREATE INDEX idx_outbox_status ON outbox(status) WHERE status = 'PENDING';
CREATE INDEX idx_outbox_created ON outbox(created_at);
```

## Adding Domain Events to Existing Database

```sql
-- V2__add_domain_event_tracking.sql
-- Step 1: Create domain event log table
CREATE TABLE domain_event_log (
    id SERIAL PRIMARY KEY,
    event_id VARCHAR(36) NOT NULL UNIQUE,
    event_type VARCHAR(200) NOT NULL,
    aggregate_id VARCHAR(36) NOT NULL,
    aggregate_type VARCHAR(100) NOT NULL,
    event_data JSONB NOT NULL,
    metadata JSONB DEFAULT '{}',
    occurred_at TIMESTAMPTZ NOT NULL,
    published BOOLEAN DEFAULT FALSE
);

-- Step 2: Add migration tracking to existing tables
ALTER TABLE orders ADD COLUMN IF NOT EXISTS ddd_version INT DEFAULT 0;
ALTER TABLE orders ADD COLUMN IF NOT EXISTS last_domain_event_at TIMESTAMPTZ;

-- Step 3: Backfill past data (if needed)
INSERT INTO domain_event_log (
    event_id, event_type, aggregate_id, aggregate_type,
    event_data, occurred_at, published
)
SELECT
    gen_random_uuid()::text,
    'OrderMigrated',
    id::text,
    'Order',
    jsonb_build_object(
        'order_id', id,
        'status', status,
        'total_amount', total_amount
    ),
    created_at,
    TRUE
FROM orders
WHERE NOT EXISTS (
    SELECT 1 FROM domain_event_log
    WHERE aggregate_id = orders.id::text
    AND event_type = 'OrderMigrated'
);
```

## CQRS Read Model Table Migration

```sql
-- V3__create_order_read_model.sql
-- Materialized view for CQRS query side
CREATE MATERIALIZED VIEW order_summary_mv AS
SELECT
    o.id,
    o.customer_id,
    o.status,
    o.total_amount,
    COUNT(oi.id) AS item_count,
    o.created_at,
    o.updated_at
FROM orders o
LEFT JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id;

CREATE UNIQUE INDEX idx_order_summary_mv_id ON order_summary_mv(id);

-- Refresh function
CREATE OR REPLACE FUNCTION refresh_order_summary()
RETURNS TRIGGER AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY order_summary_mv;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Trigger on domain events
CREATE TRIGGER refresh_order_summary_on_event
    AFTER INSERT OR UPDATE ON domain_event_log
    FOR EACH STATEMENT
    EXECUTE FUNCTION refresh_order_summary();
```

## Idempotent Migration Scripts

```sql
-- V4__add_event_store_if_not_exists.sql
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name = 'event_store'
    ) THEN
        CREATE TABLE event_store (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            stream_id VARCHAR(100) NOT NULL,
            stream_version INT NOT NULL,
            event_type VARCHAR(200) NOT NULL,
            event_data JSONB NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            UNIQUE(stream_id, stream_version)
        );
        RAISE NOTICE 'Created event_store table';
    ELSE
        RAISE NOTICE 'event_store table already exists, skipping';
    END IF;
END $$;
```

## Backward-Compatible Schema Changes

```sql
-- V5__add_event_metadata_column.sql
-- Step 1: Add column as nullable (backward compatible)
ALTER TABLE domain_event_log
    ADD COLUMN IF NOT EXISTS correlation_id VARCHAR(64);

-- Step 2: Populate existing rows
UPDATE domain_event_log
SET correlation_id = metadata->>'correlation_id'
WHERE correlation_id IS NULL
  AND metadata ? 'correlation_id';

-- Step 3: Add NOT NULL constraint (after backfill)
ALTER TABLE domain_event_log
    ALTER COLUMN correlation_id SET NOT NULL;

-- Step 4: Add index
CREATE INDEX IF NOT EXISTS idx_event_correlation
    ON domain_event_log(correlation_id);
```

## Rollback Strategy

```sql
-- V5__rollback_plan.sql
-- Rollback: Drop event tracking columns from orders
-- ALTER TABLE orders DROP COLUMN IF EXISTS ddd_version;
-- ALTER TABLE orders DROP COLUMN IF EXISTS last_domain_event_at;

-- Rollback: Drop event store
-- DROP TABLE IF EXISTS event_store CASCADE;

-- Rollback: Drop outbox
-- DROP TABLE IF EXISTS outbox CASCADE;

-- Rollback: Drop domain event log
-- DROP TABLE IF EXISTS domain_event_log CASCADE;
```
