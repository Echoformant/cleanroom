-- Key Registry Schema for SQLite
-- The identity spine for all VECTOR 1 / Clearlane operations

CREATE TABLE IF NOT EXISTS key_registry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_name TEXT NOT NULL,
    uei TEXT,                           -- Unique Entity Identifier (SAM.gov)
    ein TEXT,                           -- Employer Identification Number
    assistance_listing TEXT,            -- Pipe-delimited AL/CFDA codes (e.g., "93.958|93.959")
    state_fund_code TEXT,               -- Pipe-delimited state codes (e.g., "DHS-DAABHS-GR|DHS-OBHS-MEDICAID")
    duns_legacy TEXT,                   -- Legacy DUNS number (nullable)
    aka_names TEXT,                     -- Pipe-delimited aliases
    status TEXT CHECK (status IN ('active', 'retired')) DEFAULT 'active',
    source_of_truth TEXT,               -- Editor + evidence citation
    valid_from DATE,
    valid_to DATE,                      -- NULL = currently valid
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for common join patterns
CREATE INDEX IF NOT EXISTS idx_key_registry_uei ON key_registry(uei) WHERE uei IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_key_registry_ein ON key_registry(ein) WHERE ein IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_key_registry_status ON key_registry(status);

-- Trigger to update timestamp
CREATE TRIGGER IF NOT EXISTS key_registry_updated 
AFTER UPDATE ON key_registry
BEGIN
    UPDATE key_registry SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- =============================================================================
-- Join Surface View (flattens arrays for easy joins)
-- =============================================================================
-- Note: SQLite doesn't have unnest(), so we use this for lookups instead
-- For PostgreSQL, use the unnest version in the README

CREATE VIEW IF NOT EXISTS v_key_registry_active AS
SELECT 
    id,
    entity_name,
    uei,
    ein,
    assistance_listing,
    state_fund_code,
    duns_legacy,
    aka_names,
    source_of_truth,
    valid_from,
    valid_to
FROM key_registry
WHERE status = 'active'
  AND (valid_to IS NULL OR valid_to > DATE('now'));

-- =============================================================================
-- Helper: Check if an entity matches by any key
-- =============================================================================
-- Usage: SELECT * FROM key_registry WHERE match_any_key('93.958', '71-0499465', 'DHS-DAABHS-GR')

-- For SQLite, we do this with LIKE patterns on pipe-delimited fields:
-- SELECT * FROM key_registry 
-- WHERE assistance_listing LIKE '%93.958%' 
--    OR ein = '71-0499465'
--    OR state_fund_code LIKE '%DHS-DAABHS-GR%';

-- =============================================================================
-- Sample data insert
-- =============================================================================
INSERT OR IGNORE INTO key_registry (entity_name, uei, ein, assistance_listing, state_fund_code, aka_names, status, source_of_truth, valid_from)
VALUES 
    ('NAMI Arkansas Inc', NULL, '71-0499465', NULL, NULL, 'NAMI AR|National Alliance on Mental Illness - Arkansas', 'active', 'Editor: [pending]', '2024-07-01'),
    ('Arkansas Department of Human Services', NULL, NULL, '93.958|93.959|93.778', 'DHS-DAABHS-GR|DHS-OBHS-MEDICAID', 'DHS|AR DHS', 'active', 'Editor: [pending]', '2020-01-01'),
    ('Arkansas Administrative Office of the Courts', NULL, NULL, '16.585|16.838', 'AOC-SPC-ACCT|AOC-SPECIALTY-COURT-FUND', 'AOC|AR Courts', 'active', 'Editor: [pending]', '2020-01-01'),
    ('Arkansas Recovery Peer and Recovery Organization Project', NULL, NULL, '93.243', 'DHS-ARORP', 'ARORP', 'active', 'Editor: [pending]', '2022-01-01'),
    ('Arkansas Department of Finance and Administration', NULL, NULL, NULL, 'DFA-TREASURY|DFA-OSP', 'DFA|AR DFA', 'active', 'Editor: [pending]', '2020-01-01'),
    ('Arkansas Opioid Recovery Partnership', NULL, NULL, NULL, 'OPIOID-SETTLEMENT-FUND|STATE-OPIOID-RESPONSE', 'Opioid Settlement|SOR Arkansas', 'active', 'Editor: [pending]', '2022-01-01');
