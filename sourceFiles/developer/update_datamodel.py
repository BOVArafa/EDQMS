"""
update_datamodel.py
Reads dashboard-reports-analysis.md + current datamodel.json,
sends them to Claude Opus 4.8 with a structured prompt, and writes
the fully updated datamodel.json to disk.

Usage (pick one):
    # Option 1 — .env file (recommended, created once):
    echo 'ANTHROPIC_API_KEY=sk-ant-...' > sourceFiles/developer/.env
    python3 sourceFiles/developer/update_datamodel.py

    # Option 2 — inline CLI flag:
    python3 sourceFiles/developer/update_datamodel.py --api-key sk-ant-...

    # Option 3 — export in the same shell, then run:
    export ANTHROPIC_API_KEY=sk-ant-... && python3 sourceFiles/developer/update_datamodel.py
"""

import argparse
import json
import os
import pathlib
import sys
import anthropic

BASE = pathlib.Path(__file__).parent

# ─── API KEY RESOLUTION ───────────────────────────────────────────────────────
# Priority: --api-key flag → ANTHROPIC_API_KEY env var → .env file in BASE dir

def _load_dotenv(path: pathlib.Path) -> None:
    """Minimal .env loader (no dependencies beyond stdlib)."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:  # don't override existing env vars
            os.environ[key] = value

def resolve_api_key(cli_key) -> str:
    if cli_key:
        return cli_key
    # Try env var first (may already be set)
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    # Fall back to .env file next to this script
    _load_dotenv(BASE / ".env")
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        sys.exit(
            "\n[ERROR] No API key found.\n"
            "Set it with one of:\n"
            "  • Create a .env file: echo 'ANTHROPIC_API_KEY=sk-ant-...' > sourceFiles/developer/.env\n"
            "  • Pass it inline: python3 update_datamodel.py --api-key sk-ant-...\n"
            "  • Export it in the same shell then run the script\n"
        )
    return key

SPEC_FILE    = BASE / "dashboard-reports-analysis.md"
INPUT_JSON   = BASE / "datamodel.json"
OUTPUT_JSON  = BASE / "datamodel_updated.json"

# ─── SYSTEM PROMPT ──────────────────────────────────────────────────────────

SYSTEM = """
You are an expert data model architect for EDQMS (Event Driven Quality
Management System), a quality management platform aligned with ISO 9001:2015.

Your task is to produce a fully updated `datamodel.json` based on a
specification document. The specification contains Obsidian-style callouts
that define corrections, rules, and report definitions. Apply every callout
exactly as described below.

═══════════════════════════════════════════════════════════════════
CALLOUT LEGEND — apply in strict priority order (highest first)
═══════════════════════════════════════════════════════════════════

1. [!bug]      → MANDATORY correction. Overrides any base attribute list or
                 report spec for the affected entity. Insert / Update / Delete
                 attributes exactly as listed in the callout body.

2. [!warning]  → Architectural constraint. Respect it when shaping descriptions
                 or attribute notes; it does not change the JSON schema.
                 EXCEPTION: the first [!warning] at the top of the document
                 ("Ignore EDQMS-01_DataModel_DesignRationale") is a global rule —
                 use ONLY the specification document as your source of truth.

3. [!important] → Global design rule applied to ALL tables:
                  - ROLLUP COLUMNS: whenever a table's PK is used as an FK in
                    another table, the first table must have a rollup attribute
                    listing child records (if one is not already present in the
                    spec).
                  - MIRROR COLUMNS: a mirror copies one attribute from a rollup-
                    referenced table. Type syntax: mirror: DISTINCT("table"."attr")
                  - Control module tables have no new-item forms; they are
                    query views of existing data — note this in their description.

4. [!tip]      → Report override. Replaces the base Report spec for the same
                 report slot (Report-A or Report-B). If the tip defines a new
                 report that does not match an existing slot, add it as Report-A
                 if there is none, otherwise add as Report-B.
                 Normalize "pizza" graph_type to "donut".
                 For unspecified graph_type in a tip, infer the best match from
                 the Graph Type Reference in the spec.

5. [!abstract] → Conceptual redefinition. Update the entity's "description"
                 field to reflect the new definition. Summarise in English even
                 if the callout is in Portuguese.

6. [!note]     → Context or exclusion notice. "Sem necessidade de Reports" means
                 set both Report-A and Report-B to null for that table.

═══════════════════════════════════════════════════════════════════
ATTRIBUTE TYPE CONVENTIONS (canonical list for the output JSON)
═══════════════════════════════════════════════════════════════════

PK | string | text | int | decimal | bool | date | datetime
enum: A/B/C                    — single-select from fixed list
FK → Table (display: field)    — lookup
rollup → Table (via: FK field) — computed list of child records
computed: formula              — derived, not user-editable
mirror: DISTINCT("table"."attr")  — copies one attribute via a rollup link
multivalued                    — can hold multiple values
attachment                     — file or link attachment field

═══════════════════════════════════════════════════════════════════
OUTPUT JSON SCHEMA
═══════════════════════════════════════════════════════════════════

{
  "modules": {
    "ModuleName": {
      "tables": {
        "TableName": {
          "visibility": "show",           // always "show" unless entity is a
                                          // pure lookup (keep existing value)
          "description": "...",           // update per [!abstract] callouts
          "attributes": [
            {
              "name": "attributeName",
              "type": "...",              // use canonical types above
              "notes": "..."             // optional; omit if empty
            }
          ],
          "reports": {                   // null if [!note] says no reports
            "Report-A": {
              "graph_type": "...",       // from Graph Type Reference
              "rule": "...",            // for all non-table chart types
              "filters": ["key1", ...]
            },
            "Report-B": {
              "graph_type": "...",
              "query": "...",           // use "query" instead of "rule" for
                                        // graph_type = "table"
              "filters": ["key1", ...]
            }
          }
        }
      }
    }
  }
}

Rules:
- Use "rule" for chart reports, "query" for graph_type "table" reports.
  Never include both in the same report object.
- If a report slot is not needed, set it to null (not an empty object).
- If ALL reports for a table are null, set "reports" to null.
- Preserve the exact module and table names from the current datamodel.json.
- New tables required by the spec:
    • Talent module  → add Squads, Onboarding
    • NEW Quality module (append after Talent) → add Risks, Sources,
      Source Categories, Requirements, actionApplication, Event Log

═══════════════════════════════════════════════════════════════════
REPORT HANDLING SPECIAL CASES
═══════════════════════════════════════════════════════════════════

Tasks   → Report-B is replaced by the [!tip] at line ~294: bar chart
          showing executionTime vs realExecutionTime gap (top 10 most
          critical), sorted ascending by gap, filters: processName,
          roles, productName, scopeName.

Events  → Both base reports are replaced by the [!tip] at line ~335:
          single Report-A bar chart — open ticket count grouped by
          eventName per factory; filters: factoryName, productName,
          scopeName. Set Report-B to null.

Processes → Report-B is removed ([!tip] line ~377 says only Report-A).
            [!tip] overrides Report-A filters to: productName, scopeName,
            design.

Forecasts → Report-B is not needed ([!note] line ~185).

Activities, Workflows, Actions, Constraints, Handouts, Channels,
Product Scopes, Scopes, Products, Product Class, Product Groups,
Source Categories, actionApplication → no dedicated reports (null).

Roles → Report-B is replaced by [!tip] line ~1026: donut chart —
        count of tasks grouped by roleName where headCount > 0;
        filter: levelName.

Tickets → Report-B is replaced by [!tip]: donut chart — count of
          tickets grouped by scopeName; filters: customerName, period,
          constraintName.

Projects → Report-A (Real vs Estimated Execution) has no graph_type
           specified in [!tip]; use "bar" (estimated vs real execution
           time per project).

Productivity → Report-C and Report-D are [!tip] additions but lack
               graph_type. Use "bar" for Report-C (task count by
               levelRank), "line" for Report-D (marginal productivity
               simulation). Add them as Report-C and Report-D keys.
"""

# ─── USER MESSAGE ────────────────────────────────────────────────────────────

def build_user_message(spec_text: str, current_json: str) -> str:
    return f"""
Below are the two files you must work from.

<specification filename="dashboard-reports-analysis.md">
{spec_text}
</specification>

<current_datamodel filename="datamodel.json">
{current_json}
</current_datamodel>

Produce the complete updated `datamodel.json`.

Apply every [!bug], [!tip], [!warning], [!abstract], [!important], and [!note]
callout following the rules in the system prompt.

For each table:
1. Start from the "Complete attribute list" in the spec (not the current JSON,
   which has no attributes yet) — this is the base attribute list.
2. Apply all [!bug] Attributes changes (Insert / Update / Delete) on top.
3. Fill in or override reports using the spec Report-A / Report-B definitions,
   then apply any [!tip] overrides.
4. Update "description" if an [!abstract] redefines the entity.
5. Preserve the module structure and table names exactly.

Output ONLY valid JSON — no markdown fences, no commentary, no explanation.
Start your response with {{ and end with }}.
"""

# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Update datamodel.json via Claude Opus 4.8")
    parser.add_argument("--api-key", metavar="KEY", help="Anthropic API key (overrides env var and .env file)")
    args = parser.parse_args()

    api_key = resolve_api_key(args.api_key)

    spec_text    = SPEC_FILE.read_text(encoding="utf-8")
    current_json = INPUT_JSON.read_text(encoding="utf-8")

    client = anthropic.Anthropic(api_key=api_key)

    print("Sending request to Claude Opus 4.8 …")

    collected = []

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=32000,
        thinking={"type": "adaptive"},
        system=[
            {
                "type": "text",
                "text": SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": build_user_message(spec_text, current_json),
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
            }
        ],
    ) as stream:
        for event in stream:
            # Print text deltas to console so you can watch progress
            if hasattr(event, "type"):
                if event.type == "content_block_delta":
                    delta = event.delta
                    if hasattr(delta, "type") and delta.type == "text_delta":
                        print(delta.text, end="", flush=True)
                        collected.append(delta.text)

    print("\n\nStream complete.")

    raw_output = "".join(collected).strip()

    # Strip any accidental markdown fences the model might still emit
    if raw_output.startswith("```"):
        raw_output = raw_output.split("\n", 1)[1]
    if raw_output.endswith("```"):
        raw_output = raw_output.rsplit("```", 1)[0]
    raw_output = raw_output.strip()

    # Validate JSON before writing
    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError as exc:
        print(f"\n⚠ Output is not valid JSON: {exc}")
        fallback = OUTPUT_JSON.with_suffix(".raw.txt")
        fallback.write_text(raw_output, encoding="utf-8")
        print(f"  Raw output saved to {fallback}")
        return

    OUTPUT_JSON.write_text(
        json.dumps(parsed, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n✓ Updated data model written to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
