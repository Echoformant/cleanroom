#!/usr/bin/env python3
"""
Composite Schema Cycling Tool for Arkansas Public-Finance Artifacts

Implements the Composite Schema Cycling methodology:
1. Start with an anchor artifact (usually authority_reference or money_flow)
2. Generate a composite schema with the anchor + empty slots for other 3 types
3. Output for LLM to fill the empty slots
4. Track which artifacts have been used in this cycle (no reuse)
5. Rotate the anchor through all 4 types = 1 complete cycle

Usage:
  python schema_cycler.py anchor <artifact_id>      # Start a new cycle with anchor
  python schema_cycler.py continue <cycle_id>       # Continue an existing cycle
  python schema_cycler.py status <cycle_id>         # Show cycle status
  python schema_cycler.py list                      # List all cycles
  python schema_cycler.py ingest <cycle_id> <file>  # Ingest LLM response

See docs/composite_schema_cycling.md for methodology.
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional
import uuid
import urllib.request
import urllib.error

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
CYCLES_DIR = BASE_DIR / "_cycles"
ARTIFACTS_DIRS = {
    "money_flow": BASE_DIR / "money_flow",
    "authority_reference": BASE_DIR / "authority_reference", 
    "evidence_item": BASE_DIR / "evidence_item",
    "field_validation": BASE_DIR / "field_validation"
}

# Category order for cycling
CYCLE_ORDER = ["authority_reference", "money_flow", "evidence_item", "field_validation"]

# Schema templates (empty slots)
SCHEMA_TEMPLATES = {
    "money_flow": {
        "flow_id": "[FILL - unique ID starting with MF- or AR_FY]",
        "source": "[FILL - funding source entity]",
        "intermediary": "[FILL - pass-through entity or 'None']",
        "destination": "[FILL - receiving entity]",
        "amount": 0,
        "fund_type": "[FILL - 'state' or 'federal']",
        "fiscal_year": "[FILL - e.g., '2026' or '2025-2026']",
        "restrictions": {
            "medicaid": False,
            "dhs_controlled": False
        },
        "statutory_basis": "[FILL - legal authority citation]",
        "editor_status": "pending"
    },
    "authority_reference": {
        "authority_id": "[FILL - unique ID starting with AUTH- or AR-AUTH-]",
        "authority_type": "[FILL - 'statute', 'regulation', or 'policy']",
        "citation": "[FILL - formal citation]",
        "administering_body": "[FILL - agency/entity with authority]",
        "governs": ["[FILL - what this authority governs]"],
        "effects": {
            "access_limiting": False,
            "appeal_mechanism": False
        },
        "editor_status": "pending"
    },
    "evidence_item": {
        "evidence_id": "[FILL - unique ID starting with EVID- or EV-]",
        "section": "[FILL - reference to related flow or authority]",
        "claim_summary": "[FILL - what this evidence supports]",
        "evidence_type": "[FILL - 'statute', 'budget', 'grant', 'administrative_rule', or 'field_validation']",
        "source": {
            "title": "[FILL - document title]",
            "issuing_body": "[FILL - issuing organization]",
            "url": "[FILL - source URL if available]"
        },
        "confidence_level": "[FILL - 'high', 'medium', or 'low']",
        "editor_status": "pending"
    },
    "field_validation": {
        "fv_id": "[FILL - unique ID starting with FV-]",
        "jurisdiction": "Arkansas",
        "validating_entity": "[FILL - entity that performed validation]",
        "alignment_status": "[FILL - 'open', 'mixed', or 'captured']",
        "evidence_basis": ["[FILL - list of supporting artifact IDs]"],
        "disclosure_level": "restricted",
        "editor_status": "pending"
    }
}


def load_artifact(artifact_id: str) -> Optional[dict]:
    """Load an artifact by ID from any category."""
    for category, cat_path in ARTIFACTS_DIRS.items():
        if not cat_path.exists():
            continue
        
        for item in cat_path.iterdir():
            if item.name.startswith(".") or "batch" in item.name.lower():
                continue
            
            artifact = None
            if item.is_file() and item.suffix == ".json":
                try:
                    with open(item, "r", encoding="utf-8") as f:
                        artifact = json.load(f)
                except:
                    continue
            elif item.is_dir():
                inner = item / "0.json"
                if inner.exists():
                    try:
                        with open(inner, "r", encoding="utf-8") as f:
                            artifact = json.load(f)
                    except:
                        continue
            
            if artifact:
                aid = artifact.get("flow_id") or artifact.get("authority_id") or \
                      artifact.get("evidence_id") or artifact.get("fv_id")
                if aid == artifact_id:
                    return {"category": category, "data": artifact}
    
    return None


def get_category_for_artifact(artifact: dict) -> str:
    """Determine category from artifact data."""
    if "flow_id" in artifact:
        return "money_flow"
    elif "authority_id" in artifact:
        return "authority_reference"
    elif "evidence_id" in artifact:
        return "evidence_item"
    elif "fv_id" in artifact:
        return "field_validation"
    return "unknown"


def create_composite_schema(anchor_artifact: dict, anchor_category: str, 
                           used_artifacts: List[str]) -> dict:
    """
    Create a composite schema with the anchor and empty slots for other types.
    """
    composite = {
        "_cycle_metadata": {
            "anchor_category": anchor_category,
            "anchor_id": get_artifact_id(anchor_artifact),
            "used_artifacts": used_artifacts,
            "instruction": "Fill the empty schema slots below. Do not reuse artifacts listed in used_artifacts."
        },
        "anchor": {
            "category": anchor_category,
            "artifact": anchor_artifact
        },
        "slots": {}
    }
    
    # Add empty slots for other categories
    for category in CYCLE_ORDER:
        if category != anchor_category:
            composite["slots"][category] = {
                "instruction": f"Fill this {category} schema based on the anchor artifact",
                "template": SCHEMA_TEMPLATES[category]
            }
    
    return composite


def get_artifact_id(artifact: dict) -> str:
    """Extract ID from artifact regardless of type."""
    return artifact.get("flow_id") or artifact.get("authority_id") or \
           artifact.get("evidence_id") or artifact.get("fv_id") or "unknown"


def create_new_cycle(artifact_id: str) -> dict:
    """Start a new cycle with the given artifact as anchor."""
    CYCLES_DIR.mkdir(exist_ok=True)
    
    # Load the anchor artifact
    result = load_artifact(artifact_id)
    if not result:
        print(f"❌ Artifact '{artifact_id}' not found")
        return None
    
    anchor_category = result["category"]
    anchor_artifact = result["data"]
    
    # Generate cycle ID
    cycle_id = f"CYCLE-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
    
    # Initialize cycle state
    cycle_state = {
        "cycle_id": cycle_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "active",
        "current_turn": 1,
        "current_anchor_category": anchor_category,
        "original_anchor_id": artifact_id,
        "turns_completed": [],
        "used_artifacts": [artifact_id],
        "generated_artifacts": []
    }
    
    # Create composite schema for Turn 1
    composite = create_composite_schema(anchor_artifact, anchor_category, [artifact_id])
    
    # Save cycle state
    cycle_dir = CYCLES_DIR / cycle_id
    cycle_dir.mkdir(exist_ok=True)
    
    with open(cycle_dir / "state.json", "w", encoding="utf-8") as f:
        json.dump(cycle_state, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    # Save Turn 1 prompt
    with open(cycle_dir / "turn_1_prompt.json", "w", encoding="utf-8") as f:
        json.dump(composite, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    # Create empty response file as placeholder
    empty_response = {
        "_instructions": "Paste LLM response here, replacing this entire object. Expected structure: { slots: { category: { artifact: {...} } } }",
        "slots": {}
    }
    with open(cycle_dir / "turn_1_response.json", "w", encoding="utf-8") as f:
        json.dump(empty_response, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    print(f"\n{'='*80}")
    print(f"🔄 New Cycle Created: {cycle_id}")
    print(f"{'='*80}")
    print(f"\nAnchor: {artifact_id} ({anchor_category})")
    print(f"Turn: 1 of 4")
    print(f"\n📄 Prompt file: {cycle_dir / 'turn_1_prompt.json'}")
    print(f"📝 Response file: {cycle_dir / 'turn_1_response.json'} (paste LLM output here)")
    print(f"\nNext steps:")
    print(f"  1. Copy the contents of turn_1_prompt.json")
    print(f"  2. Send to LLM with instruction to fill the slots")
    print(f"  3. Paste LLM response into turn_1_response.json")
    print(f"  4. Run: python schema_cycler.py ingest {cycle_id} turn_1_response.json")
    
    return cycle_state


def load_cycle(cycle_id: str) -> Optional[dict]:
    """Load an existing cycle state."""
    cycle_dir = CYCLES_DIR / cycle_id
    state_file = cycle_dir / "state.json"
    
    if not state_file.exists():
        print(f"❌ Cycle '{cycle_id}' not found")
        return None
    
    with open(state_file, "r", encoding="utf-8") as f:
        return json.load(f)


def continue_cycle(cycle_id: str) -> dict:
    """Generate the next turn's prompt for a cycle."""
    cycle_state = load_cycle(cycle_id)
    if not cycle_state:
        return None
    
    if cycle_state["status"] == "completed":
        print(f"✅ Cycle {cycle_id} is already completed")
        return cycle_state
    
    current_turn = cycle_state["current_turn"]
    
    # Determine next anchor category
    current_idx = CYCLE_ORDER.index(cycle_state["current_anchor_category"])
    next_idx = (current_idx + 1) % len(CYCLE_ORDER)
    next_category = CYCLE_ORDER[next_idx]
    
    # Find the artifact to use as next anchor (from last turn's generated artifacts)
    last_turn_artifacts = [a for a in cycle_state["generated_artifacts"] 
                          if a.get("turn") == current_turn and a.get("category") == next_category]
    
    if not last_turn_artifacts:
        print(f"⚠️  No {next_category} artifact was generated in turn {current_turn}")
        print(f"   Cannot continue cycle without a {next_category} to use as anchor")
        return cycle_state
    
    next_anchor = last_turn_artifacts[0]["data"]
    next_anchor_id = get_artifact_id(next_anchor)
    
    # Update state
    cycle_state["current_turn"] = current_turn + 1
    cycle_state["current_anchor_category"] = next_category
    cycle_state["used_artifacts"].append(next_anchor_id)
    
    if cycle_state["current_turn"] > 4:
        cycle_state["status"] = "completed"
        print(f"\n✅ Cycle {cycle_id} completed after 4 turns!")
    else:
        # Generate next prompt
        composite = create_composite_schema(next_anchor, next_category, 
                                           cycle_state["used_artifacts"])
        
        cycle_dir = CYCLES_DIR / cycle_id
        turn_num = cycle_state['current_turn']
        prompt_file = f"turn_{turn_num}_prompt.json"
        response_file = f"turn_{turn_num}_response.json"
        
        with open(cycle_dir / prompt_file, "w", encoding="utf-8") as f:
            json.dump(composite, f, indent=2, ensure_ascii=False)
            f.write("\n")
        
        # Create empty response file as placeholder
        empty_response = {
            "_instructions": "Paste LLM response here, replacing this entire object. Expected structure: { slots: { category: { artifact: {...} } } }",
            "slots": {}
        }
        with open(cycle_dir / response_file, "w", encoding="utf-8") as f:
            json.dump(empty_response, f, indent=2, ensure_ascii=False)
            f.write("\n")
        
        print(f"\n{'='*80}")
        print(f"🔄 Cycle Continued: {cycle_id}")
        print(f"{'='*80}")
        print(f"\nNew Anchor: {next_anchor_id} ({next_category})")
        print(f"Turn: {turn_num} of 4")
        print(f"\n📄 Prompt file: {cycle_dir / prompt_file}")
        print(f"📝 Response file: {cycle_dir / response_file} (paste LLM output here)")
    
    # Save updated state
    cycle_dir = CYCLES_DIR / cycle_id
    with open(cycle_dir / "state.json", "w", encoding="utf-8") as f:
        json.dump(cycle_state, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    return cycle_state


def ingest_response(cycle_id: str, response_file: str):
    """Ingest an LLM response and extract generated artifacts."""
    cycle_state = load_cycle(cycle_id)
    if not cycle_state:
        return None
    
    cycle_dir = CYCLES_DIR / cycle_id
    response_path = cycle_dir / response_file
    
    if not response_path.exists():
        # Try as absolute path
        response_path = Path(response_file)
        if not response_path.exists():
            print(f"❌ Response file not found: {response_file}")
            return None
    
    with open(response_path, "r", encoding="utf-8") as f:
        response = json.load(f)
    
    current_turn = cycle_state["current_turn"]
    
    # Extract artifacts from response
    # Expected structure: {"slots": {"category": {"artifact": {...}}}}
    slots = response.get("slots", {})
    
    for category, slot_data in slots.items():
        artifact = slot_data.get("artifact") or slot_data.get("template")
        if artifact and "[FILL" not in json.dumps(artifact):
            artifact_id = get_artifact_id(artifact)
            
            cycle_state["generated_artifacts"].append({
                "turn": current_turn,
                "category": category,
                "id": artifact_id,
                "data": artifact
            })
            
            # Save artifact to _stubs for review
            stubs_dir = BASE_DIR / "_stubs" / f"cycle_{cycle_id}"
            stubs_dir.mkdir(parents=True, exist_ok=True)
            
            with open(stubs_dir / f"{artifact_id}.json", "w", encoding="utf-8") as f:
                json.dump(artifact, f, indent=2, ensure_ascii=False)
                f.write("\n")
            
            print(f"  ✓ Extracted {category}: {artifact_id}")
    
    # Mark turn as completed
    cycle_state["turns_completed"].append(current_turn)
    
    # Save updated state
    with open(cycle_dir / "state.json", "w", encoding="utf-8") as f:
        json.dump(cycle_state, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    print(f"\n✓ Turn {current_turn} ingested")
    print(f"  Generated artifacts saved to: {BASE_DIR / '_stubs' / f'cycle_{cycle_id}'}")
    print(f"\nNext: Run 'python schema_cycler.py continue {cycle_id}' to generate next turn")
    
    return cycle_state


def show_status(cycle_id: str):
    """Show the status of a cycle."""
    cycle_state = load_cycle(cycle_id)
    if not cycle_state:
        return
    
    print(f"\n{'='*80}")
    print(f"📊 Cycle Status: {cycle_id}")
    print(f"{'='*80}")
    print(f"\nStatus: {cycle_state['status']}")
    print(f"Created: {cycle_state['created_at']}")
    print(f"Original Anchor: {cycle_state['original_anchor_id']}")
    print(f"Current Turn: {cycle_state['current_turn']}")
    print(f"Current Anchor Category: {cycle_state['current_anchor_category']}")
    
    print(f"\nUsed Artifacts ({len(cycle_state['used_artifacts'])}):")
    for aid in cycle_state['used_artifacts']:
        print(f"  • {aid}")
    
    print(f"\nGenerated Artifacts ({len(cycle_state['generated_artifacts'])}):")
    for art in cycle_state['generated_artifacts']:
        print(f"  Turn {art['turn']}: {art['id']} ({art['category']})")
    
    print(f"\nTurns Completed: {cycle_state['turns_completed']}")


def list_cycles():
    """List all cycles."""
    if not CYCLES_DIR.exists():
        print("No cycles found")
        return
    
    cycles = []
    for item in CYCLES_DIR.iterdir():
        if item.is_dir():
            state_file = item / "state.json"
            if state_file.exists():
                with open(state_file, "r", encoding="utf-8") as f:
                    state = json.load(f)
                cycles.append(state)
    
    if not cycles:
        print("No cycles found")
        return
    
    print(f"\n{'='*80}")
    print(f"📋 All Cycles ({len(cycles)} total)")
    print(f"{'='*80}\n")
    
    for cycle in sorted(cycles, key=lambda x: x["created_at"], reverse=True):
        status_icon = "✅" if cycle["status"] == "completed" else "🔄"
        print(f"{status_icon} {cycle['cycle_id']}")
        print(f"   Status: {cycle['status']} | Turn: {cycle['current_turn']}/4")
        print(f"   Anchor: {cycle['original_anchor_id']}")
        print(f"   Generated: {len(cycle['generated_artifacts'])} artifacts")
        print()


def run_ollama_turn(cycle_id: str, model: str = "llama3.2"):
    """Run the current turn through Ollama and auto-ingest the response."""
    cycle_state = load_cycle(cycle_id)
    if not cycle_state:
        return None
    
    if cycle_state["status"] == "completed":
        print(f"✅ Cycle {cycle_id} is already completed")
        return cycle_state
    
    current_turn = cycle_state["current_turn"]
    cycle_dir = CYCLES_DIR / cycle_id
    prompt_file = cycle_dir / f"turn_{current_turn}_prompt.json"
    
    if not prompt_file.exists():
        print(f"❌ Prompt file not found: {prompt_file}")
        return None
    
    # Load the prompt
    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt_data = json.load(f)
    
    # Build the LLM prompt
    system_prompt = """You are an artifact extraction assistant for Operation NAMI Clearlane. 
Your task is to generate schema-valid JSON artifacts based on an anchor artifact.

Rules:
- Output ONLY valid JSON matching the expected structure
- Set editor_status to "pending" for all generated artifacts
- Do NOT add fields not in the schema
- Do NOT add commentary or explanation outside the JSON
- If you cannot determine a field value, use "[UNKNOWN - requires research]"

ID Naming Conventions:
- money_flow: Start with MF-AR- or AR_FY
- authority_reference: Start with AUTH-AR- or AR-AUTH-
- evidence_item: Start with EVID-AR- or EV-AR-
- field_validation: Start with FV-AR-"""

    user_prompt = f"""Given this composite schema, fill each slot with a plausible artifact related to the anchor.

{json.dumps(prompt_data, indent=2)}

Return ONLY a JSON object with this structure (no markdown, no explanation):
{{
  "slots": {{
    "<category>": {{
      "artifact": {{ ... filled artifact ... }}
    }}
  }}
}}

Fill all three slots based on the anchor artifact."""

    print(f"\n{'='*80}")
    print(f"🤖 Running Turn {current_turn} through Ollama ({model})")
    print(f"{'='*80}")
    print(f"\nSending to Ollama...")
    
    # Call Ollama API
    try:
        request_data = json.dumps({
            "model": model,
            "prompt": f"{system_prompt}\n\n{user_prompt}",
            "stream": False,
            "format": "json"
        }).encode("utf-8")
        
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=request_data,
            headers={"Content-Type": "application/json"}
        )
        
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        
        response_text = result.get("response", "")
        
    except urllib.error.URLError as e:
        print(f"❌ Failed to connect to Ollama: {e}")
        print("   Make sure Ollama is running: ollama serve")
        return None
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return None
    
    # Parse the response
    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        import re
        json_match = re.search(r'\{[\s\S]*\}', response_text)
        if json_match:
            try:
                response_json = json.loads(json_match.group())
            except:
                print(f"❌ Could not parse Ollama response as JSON")
                print(f"   Response: {response_text[:500]}...")
                # Save raw response for debugging
                raw_file = cycle_dir / f"turn_{current_turn}_raw_response.txt"
                with open(raw_file, "w", encoding="utf-8") as f:
                    f.write(response_text)
                print(f"   Raw response saved to: {raw_file}")
                return None
        else:
            print(f"❌ No JSON found in Ollama response")
            return None
    
    # Save the response
    response_file = cycle_dir / f"turn_{current_turn}_response.json"
    with open(response_file, "w", encoding="utf-8") as f:
        json.dump(response_json, f, indent=2, ensure_ascii=False)
        f.write("\n")
    
    print(f"✓ Response saved to: {response_file}")
    
    # Now ingest it
    print(f"\nIngesting response...")
    ingest_response(cycle_id, str(response_file))
    
    # Ask about continuing
    print(f"\n{'='*80}")
    if cycle_state["current_turn"] < 4:
        print(f"Ready for next turn. Run:")
        print(f"  python schema_cycler.py ollama {cycle_id} --model {model}")
        print(f"\nOr generate prompt only:")
        print(f"  python schema_cycler.py continue {cycle_id}")
    
    return cycle_state


def main():
    parser = argparse.ArgumentParser(description="Composite Schema Cycling Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # anchor command
    anchor_parser = subparsers.add_parser("anchor", help="Start a new cycle with an anchor artifact")
    anchor_parser.add_argument("artifact_id", help="ID of the anchor artifact")
    
    # continue command
    continue_parser = subparsers.add_parser("continue", help="Continue an existing cycle")
    continue_parser.add_argument("cycle_id", help="ID of the cycle to continue")
    
    # status command
    status_parser = subparsers.add_parser("status", help="Show cycle status")
    status_parser.add_argument("cycle_id", help="ID of the cycle")
    
    # list command
    subparsers.add_parser("list", help="List all cycles")
    
    # ingest command
    ingest_parser = subparsers.add_parser("ingest", help="Ingest LLM response")
    ingest_parser.add_argument("cycle_id", help="ID of the cycle")
    ingest_parser.add_argument("response_file", help="Path to response JSON file")
    
    # ollama command
    ollama_parser = subparsers.add_parser("ollama", help="Run current turn through Ollama")
    ollama_parser.add_argument("cycle_id", help="ID of the cycle")
    ollama_parser.add_argument("--model", "-m", default="llama3.2", help="Ollama model to use (default: llama3.2)")
    ollama_parser.add_argument("--all", "-a", action="store_true", help="Run all remaining turns automatically")
    
    args = parser.parse_args()
    
    if args.command == "anchor":
        create_new_cycle(args.artifact_id)
    elif args.command == "continue":
        continue_cycle(args.cycle_id)
    elif args.command == "status":
        show_status(args.cycle_id)
    elif args.command == "list":
        list_cycles()
    elif args.command == "ingest":
        ingest_response(args.cycle_id, args.response_file)
    elif args.command == "ollama":
        if args.all:
            # Run all remaining turns
            cycle_state = load_cycle(args.cycle_id)
            while cycle_state and cycle_state["status"] != "completed":
                run_ollama_turn(args.cycle_id, args.model)
                continue_cycle(args.cycle_id)
                cycle_state = load_cycle(args.cycle_id)
        else:
            run_ollama_turn(args.cycle_id, args.model)
            continue_cycle(args.cycle_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
