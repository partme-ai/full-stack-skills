-- ===================================================
-- Flyway Migration: Domain Event Infrastructure
-- For an e-commerce DDD system (Order Bounded Context)
-- ===================================================

-- V1__create_domain_event_store.sql
-- Domain event store for event sourcing and audit

CREATE TABLE domain_event_store (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_version   INT NOT NULL DEFAULT 1,
    event_data      JSONB NOT NULL,
    metadata        JSONB DEFAULT '{}',
    occurred_at     TIMESTAMPTZ NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_event_store_agg ON domain_event_store(aggregate_id, aggregate_type);
CREATE INDEX idx_event_store_type ON domain_event_store(event_type);
CREATE INDEX idx_event_store_time ON domain_event_store(occurred_at DESC);

COMMENT ON TABLE domain_event_store IS 'Domain event store — append-only log of all domain events';
COMMENT ON COLUMN domain_event_store.event_data IS 'Event payload in JSONB format';
COMMENT ON COLUMN domain_event_store.metadata IS 'Correlation ID, causation ID, tenant, etc.';

-- V2__create_outbox_message.sql
-- Outbox pattern for reliable domain event publishing

CREATE TABLE outbox_message (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id        UUID NOT NULL REFERENCES domain_event_store(id),
    destination     VARCHAR(255) NOT NULL,
    partition_key   VARCHAR(64),
    payload         JSONB NOT NULL,
    headers         JSONB DEFAULT '{}',
    status          VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    retry_count     INT NOT NULL DEFAULT 0,
    max_retries     INT NOT NULL DEFAULT 3,
    last_error      TEXT,
    scheduled_at    TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    processed_at    TIMESTAMPTZ,
    UNIQUE(event_id, destination)
);

CREATE INDEX idx_outbox_pending ON outbox_message(status, scheduled_at)
    WHERE status = 'PENDING' AND (scheduled_at IS NULL OR scheduled_at <= NOW());
CREATE INDEX idx_outbox_retry ON outbox_message(status, retry_count)
    WHERE status = 'RETRYING' AND retry_count < max_retries;

COMMENT ON TABLE outbox_message IS 'Outbox for reliable domain event delivery via message broker';

-- V3__create_order_snapshot.sql
-- Event sourcing snapshots for order aggregates

CREATE TABLE order_snapshot (
    aggregate_id    VARCHAR(36) PRIMARY KEY,
    version         INT NOT NULL,
    state           JSONB NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_order_snapshot_version ON order_snapshot(version);

-- V4__create_idempotency_key.sql
-- Idempotency tracking for event consumers

CREATE TABLE idempotency_key (
    id              VARCHAR(64) PRIMARY KEY,
    consumer_id     VARCHAR(100) NOT NULL,
    event_id        UUID NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    handled_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_idempotency_lookup ON idempotency_key(consumer_id, event_id, event_type);
CREATE INDEX idx_idempotency_cleanup ON idempotency_key(handled_at);

COMMENT ON TABLE idempotency_key IS 'Tracks processed events to ensure exactly-once delivery';

-- V5__seed_initial_config.sql
-- Seed data: domain event type registry

INSERT INTO domain_event_type_registry (event_type, version, schema_version, description)
VALUES
    ('OrderCreated', 1, 1, 'Order has been created with initial items'),
    ('OrderItemAdded', 1, 1, 'Item added to existing order'),
    ('OrderItemRemoved', 1, 1, 'Item removed from order'),
    ('OrderPaid', 1, 1, 'Order payment completed'),
    ('OrderShipped', 1, 1, 'Order has been shipped'),
    ('OrderDelivered', 1, 1, 'Order delivery confirmed'),
    ('OrderCancelled', 1, 1, 'Order was cancelled')
ON CONFLICT (event_type) DO NOTHING;

-- Create domain event type registry table
CREATE TABLE IF NOT EXISTS domain_event_type_registry (
    event_type      VARCHAR(200) PRIMARY KEY,
    version         INT NOT NULL DEFAULT 1,
    schema_version  INT NOT NULL DEFAULT 1,
    description     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ===================================================
-- Rollback Script (V5__rollback.sql)
-- ===================================================
-- DROP TABLE IF EXISTS domain_event_type_registry;
-- DROP TABLE IF EXISTS idempotency_key;
-- DROP TABLE IF EXISTS order_snapshot;
-- DROP TABLE IF EXISTS outbox_message;
-- DROP TABLE IF EXISTS domain_event_store;
