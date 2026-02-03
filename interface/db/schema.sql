DROP TABLE IF EXISTS authority_reference;
CREATE TABLE authority_reference (
  authority_id TEXT,
  authority_type TEXT,
  citation TEXT,
  administering_body TEXT,
  governs TEXT,
  effects TEXT,
  editor_status TEXT,
  _raw_json TEXT,
  PRIMARY KEY (authority_id)
);
CREATE INDEX idx_authority_reference_editor_status ON authority_reference(editor_status);
DROP TABLE IF EXISTS evidence_item;
CREATE TABLE evidence_item (
  evidence_id TEXT,
  section TEXT,
  claim_summary TEXT,
  evidence_type TEXT,
  source TEXT,
  confidence_level TEXT,
  editor_status TEXT,
  _raw_json TEXT,
  PRIMARY KEY (evidence_id)
);
CREATE INDEX idx_evidence_item_editor_status ON evidence_item(editor_status);
DROP TABLE IF EXISTS money_flow;
CREATE TABLE money_flow (
  flow_id TEXT,
  source TEXT,
  intermediary TEXT,
  destination TEXT,
  amount REAL,
  fund_type TEXT,
  fiscal_year TEXT,
  restrictions TEXT,
  statutory_basis TEXT,
  editor_status TEXT,
  _raw_json TEXT,
  PRIMARY KEY (flow_id)
);
CREATE INDEX idx_money_flow_editor_status ON money_flow(editor_status);
DROP TABLE IF EXISTS field_validation;
CREATE TABLE field_validation (
  fv_id TEXT,
  jurisdiction TEXT,
  validating_entity TEXT,
  corroborator TEXT,
  alignment_status TEXT,
  evidence_basis TEXT,
  disclosure_level TEXT,
  editor_status TEXT,
  _raw_json TEXT,
  PRIMARY KEY (fv_id)
);
CREATE INDEX idx_field_validation_editor_status ON field_validation(editor_status);
