---
content-type: verification-report
subject:
  - dashboard
  - reports
  - forms
  - datamodel
  - mockup
---

# EDQMS Report & Form Feasibility Report

**Purpose.** This document records the outcome of testing the EDQMS "Global Engineering Portal"
data model against a concrete demo dataset. It answers two questions posed in
`dashboard-reports-analysis.md`:

1. **Can every report defined in `datamodel.json` actually be built?** — proven by recomputing each
   report rule from base data in `validate_mockup.py`.
2. **Can the prototype forms capture the data entry the dataset requires?** — a field-by-field check of
   which values are *user-entered* (need a form control) vs *derived* (computed/mirror/rollup, never typed).

**Artifacts**

| File | Role |
|---|---|
| `mockup_data_prototype.json` | The demo dataset (413 records across all 37 tables). Base fields only. |
| `build_mockup_data.py` | Deterministic generator that produces the dataset (regenerable). |
| `validate_mockup.py` | Referential-integrity + report-recomputation harness. |
| `datamodel.json` | Target schema (edited in place — see §3). |

**Result:** `python3 validate_mockup.py` → **37/37 reports PASS, 0 referential-integrity errors.**

---

## 1. How to reproduce

```bash
cd sourceFiles/developer
python3 build_mockup_data.py     # (re)writes mockup_data_prototype.json
python3 validate_mockup.py       # prints PASS/FAIL per report; exit 0 = all green
python3 validate_mockup.py -v    # also dumps each report's recomputed output
```

The dataset stores **only base (user-entered) fields**. Every `computed` / `mirror` / `rollup` field in
`datamodel.json` is deliberately absent from the JSON and is **recomputed by the validator** — that
recomputation is exactly what proves the field (and any report built on it) is derivable from the base data.

---

## 2. Report feasibility matrix

All reports below returned a non-empty, sensible result. "Data source" is the base-field chain the
validator walked to build the report.

| Module / Table | Report | Type | Data source (base-field chain) | Status |
|---|---|---|---|---|
| Customers / Factories | A | donut | `Factories.region` | ✅ PASS |
| Customers / Factories | B | table | `Factories` + counts over `Forecasts`, `Tickets`, `Projects` | ✅ PASS |
| Customers / Forecasts | A | line | `Forecast Scopes → Tasks.executionTime` grouped by `Forecast.periodStart` × factory | ✅ PASS |
| Customers / Forecast Scopes | A | stacked_bar | `Tasks(eventID+productScopeID).executionTime` stacked by `Tasks.roleID` | ✅ PASS |
| Customers / Forecast Scopes | B | bar | `Forecast.factoryID → Factories.region` *(edited, see §3)* | ✅ PASS |
| Operation / Tasks | A | bar | `Tasks.processID` | ✅ PASS |
| Operation / Tasks | B | bar | `Jobs.realExecutionTime − Tasks.executionTime`, top-10 overruns | ✅ PASS |
| Operation / Events | A | bar | open `Tickets.eventID` × `Tickets.customerName` | ✅ PASS |
| Operation / Processes | A | bar | `Tasks.processID → processName` | ✅ PASS |
| Workload / Tickets | A | bar | `Tickets.customerName` | ✅ PASS |
| Workload / Tickets | B | donut | `Ticket → forecastScope → productScope → Scope.scopeName` | ✅ PASS |
| Workload / Projects | A | bar | est = Σ`Tasks.executionTime`; real = Σ`Jobs.realExecutionTime`, per project | ✅ PASS |
| Workload / Jobs | A | line | `Jobs.jobStatus=Done` by `realEndDate` week | ✅ PASS |
| Workload / Jobs | B | bar | Σ`Jobs.realExecutionTime` by `People.roleID` | ✅ PASS |
| Control / Capacity | A | bar | `availableHours` vs `allocatedHours` (Σ task hours via tickets in window) by role | ✅ PASS |
| Control / Capacity | B | bar | utilization % by `Role.functionID → functionName` *(mirror added, §3)* | ✅ PASS |
| Control / Usage | A | line | Σ`Jobs.realExecutionTime` by `People.functionID` × month | ✅ PASS |
| Control / Usage | B | heatmap | `Jobs` count by `People.roleID` | ✅ PASS |
| Control / Productivity | A | donut | `output/target` efficiency buckets (<80 / 80–100 / >100) | ✅ PASS |
| Control / Productivity | C | bar | tasks where `role.levelRank > min certified levelRank` for scope+product | ✅ PASS |
| Control / Productivity | D | line | marginal makespan gain of extra head on process (simulated) | ✅ PASS |
| Talent / Roles | A | donut | Σ`Roles.quantity` by `functionID` | ✅ PASS |
| Talent / Roles | B | donut | `Tasks` count by `roleID` where `quantity>0` | ✅ PASS |
| Talent / Skill Levels | A | bar | Σ`Roles.quantity` by `skillLevelID` | ✅ PASS |
| Talent / Functions | A | bar | Σ`Roles.quantity` by `functionID` | ✅ PASS |
| Talent / Graduation | A | donut | Σ`Roles.quantity` by `Graduation.field` | ✅ PASS |
| Talent / Competence | A | heatmap | `Competence(required)` × `Onboarding.isCertified` by role×scope | ✅ PASS |
| Talent / People | A | bar | active `People.functionID` | ✅ PASS |
| Quality / Risks | A | scatter | `riskLikelihood` × `riskSeverity`, size `RPN`, colour `riskCategory` | ✅ PASS |
| Quality / Risks | B | table | open risks + `Actions.riskID` count *(FK added, §3)* | ✅ PASS |
| Quality / Sources | A | bar | `Events.sourceID → Source.sourceCategoryID` *(FK added, §3)* | ✅ PASS |
| Quality / Sources | B | table | `Source → Events(sourceID) → Risks(eventID)` chain | ✅ PASS |
| Quality / Requirements | A | donut | `Requirements.requirementType` | ✅ PASS |
| Quality / Requirements | B | table | `Requirement → Risks(requirementID)`, highest RPN | ✅ PASS |
| Quality / Event Log | A | bar | `Resolved.changedAt − Open.changedAt` buckets | ✅ PASS |
| Quality / Event Log | B | table | `Event Log` rows for a chosen event | ✅ PASS |

### Capacity Report-A worked-scenario check

The dataset embeds the exact scenario hard-coded in `dashboard-reports-analysis.md`:

- **Ticket 001** — customer `PN` (FC1), event *"Offer Calculation Requested"*, `resolutionTime` 2026-10-25.
- **Tasks 012 / 032 / 033 / 045** with executionTime **5 / 8 / 8 / 15 h** (Σ = **36 h**) and roles
  JR Electrical / SR Mechanical / JR Mechanical / SR Mechanical.
- **Forecast FO2** — `periodStart` 2026-09, `periodFinish` 2027-01 (the report window), event
  *"Offer Calculation Requested"*, referencing the same tasks (forecast scope FS01).

The validator's `SCENARIO spot-check` confirms the ticket resolves to exactly those four task IDs summing
to 36 h, so the retroactive `allocatedHours` window math in the analysis is buildable on this data.

---

## 3. `datamodel.json` edits made (and why)

Each edit was forced by a report that could not otherwise be computed. All are logged here.

| # | Table | Edit | Report(s) unblocked | Rationale |
|---|---|---|---|---|
| 1 | Operation / **Actions** | add `riskID` (FK→Risks) + `applicationID` (FK→actionApplication) | Risks-B, Requirements-B, actionApplication rollup | Actions had no link to a Risk, so "linked action count" and `Risks.actions` / `actionApplication.actions` rollups were unresolvable (ISO §6.1.2(a) direct risk→action traceability). |
| 2 | Operation / **Events** | add `sourceID` (FK→Sources) | Sources-A, Sources-B | `Sources.events` rolls up "via sourceID" and the Source→Event→Risk chain needs it; Events carried no source link. |
| 3 | Customers / **Forecast Scopes** | add `region` mirror via `forecastID→Factories.region`; fix Report-B rule | Forecast Scopes-B | The rule said "region from linked Product Scope," but region exists only on Factory. Region is now derived through the parent Forecast's factory. |
| 4 | Operation / **Processes** | remove `design` mirror + `design` filter | Processes-A | `design` was deleted from Product Scopes/Tickets during the redesign; no field could populate it. Filters are now `productName` / `scopeName`. |
| 5 | Operation / **Tasks** | Report-A filters `taskStatus`/`owner`/`period` → `eventID`/`productName`/`scopeName` | Tasks-A | Tasks are execution *templates* — they have no status, owner, or date (those live on Jobs). |
| 6 | Workload / **Tickets** | remove `priority` filter from Report-A | Tickets-A | `ticketPriority` was deleted in the redesign. |
| 7 | Control / **Usage** | add mirror attrs `functionName`, `customerName`, `squadName` (from Jobs join) | Usage-A, Usage-B | This query-view's report filters referenced dimensions that were not columns on the view. |
| 8 | Control / **Capacity** | add mirror attr `functionName` (from Role→Function) | Capacity-A, Capacity-B | Same — utilization-by-function needs the function label on the view. |
| 9 | Talent / **People** | add `roleID` (FK→Roles) | Roles rollup/overheadCost, Jobs assignee-by-role | Surfaced while building People: `Roles.people`, `Roles.overheadCost=AVG(People.personalCost via roleID)`, and the Jobs "filter assignee by task role" all require `People.roleID`, which was missing. |

> Note on **Departments**: `Capacity.departmentID`, `Usage.departmentID`, and `Productivity.teamID` point at
> a Departments table that is not modeled (it is an excluded org-structure lookup per
> `dashboard-reports-analysis.md`). Because the Control tables are read-only query-views, the mockup stores
> the human-readable grouping label (function name as "team") directly on those rows. No schema change was
> needed; noted here for transparency.

---

## 4. Form data-entry coverage

Legend: **Entry** = user types/selects it (needs a form control). **Derived** = computed/mirror/rollup —
never entered; shown read-only. Only *entry* fields need form support; the mockup supplies exactly these.

| Tab (entity) | Entry fields the form must support | Derived (read-only, not entered) |
|---|---|---|
| Forecasts | factoryID, forecastPeriod, forecastYear/Quarter/Month, periodStart, periodFinish, status, createdBy | totalEstimatedHours, forecastScopes |
| Forecast Scopes | forecastID, productScopeID, eventID, notes | processID, tasks, roles, estimatedHours, region |
| Task Templates | eventID → processID → workflowID → activityID (cascading), actionID, productScopeID, executionTime, roleID, constraints, taskInput/Output, customerName | taskName, roles(via Competence), products/scopes, ticketID |
| Events | eventTitle, eventDescription, sourceID | processes, tasks, forecastScopes, ticketID, factory/product/scope mirrors |
| Processes | processName, processSystemID, processOwner, processDescription, parentProcessID, processStatus, processVersion | targetExecutionTime, activities, tasks, product/scope mirrors |
| Activities | activityName, processID, procedureID (attachment: link + ID) | roleID (from tasks), tasks |
| Workflows | processID, activities (single-select), parentStepID | workflowName, taskID, inputs/outputs/scopes/customer/procedures/products/constraints mirrors |
| Actions | actionName, actionDescription, activityID, riskID, applicationID | taskID, activityID/workflowID mirrors |
| Constraints | constrainName, constrainDescription, constrainTypeID, isActive, regulatoryReference | — |
| Handouts | handoutName, handoutDescription, channelID, Template (attachment+title), type | taskID |
| Channels | channelName, channelOwner (text), channelStatus | handouts |
| Product Scopes | productGroupID, scopeID, isActive, createdAt | products, productClassID, businessSegment, constraintName, forecastScopes |
| Product Groups | businessSegment, products (single), productClassID (multi), isActive | — |
| Scopes / Products / Product Class | master-data string/enum fields | — |
| Tickets | projectID, customerName, eventID, forecastScopeID, ticketOwner, ticketStatus, targetDate, resolutionTime, timestamps, isEscalated, escalatedToEventID | processID, products, scopes, constraintName, taskID, jobs |
| Projects | projectName, clientName, customerName, projectOwner, projectStatus | products, ticketID, jobID, estimatedTime, executionTime |
| Jobs | taskID (template), startDate, endDate, userID (filtered by task role), predecesorJob, dependencyType, realStartDate, realEndDate, jobStatus | roleID, squadName, customerName, realExecutionTime |
| Capacity / Usage / Productivity | *(none — read-only query views; no create/edit form)* | all |
| Squads | squadName, squadType, managerName, managerEmail | people |
| Roles | roleName, functionID, skillLevelID, graduationID, quantity, isActive | overheadCost, taskName, people |
| People | userName, userEmail, location, isActive, hireDate, functionID, roleID, personalCost, squadID | onboardID |
| Onboarding | userID, isCertified toggles per competence, certifications | functionID, roleID, competenceID, scope/product/resources/constraint mirrors |
| Skill Levels / Functions / Graduation / Competence | master-data / mapping fields | rollups |
| Risks | riskTitle, riskDescription, riskCategory, riskSeverity, riskLikelihood, riskOwner, riskStatus, eventID, requirementID, riskReviewedAt | riskPriorityNumber, actions |
| Sources | sourceName, sourceCategoryID, sourceOwner, sourceDescription, isActive | events, requirements |
| Source Categories | sourceCategoryName, sourceCategoryDescription | sources |
| Requirements | requirementName, requirementDescription, sourceID, requirementType, isActive, productID | risks |
| actionApplication | applicationName, applicationDescription, isoClause | actions |
| Event Log | *(system-generated — no create/edit form)* | all |

**Conclusion.** Every entry field above is populated by base values in `mockup_data_prototype.json`, so the
redesigned forms in `claude-design-prompt.md` (cascading Task selector, conditional Forecast period fields,
attachment widgets, mirror/read-only styling, Control read-only views) have real data to bind to. No form is
asked to capture a value that the data model cannot supply, and no report depends on a value the forms cannot
enter.

---

## 5. Known simplifications (mockup scope)

- **Payload** is not a separate table here; a Task carries `productScopeID` directly, from which
  `products`/`scopes` derive. This keeps the Event→Task→ProductScope matching (used by Forecast Scope
  rollups) explicit and testable without modelling the association class.
- **Departments** are represented as function-name labels on the Control query-views (see §3 note).
- **Productivity Report-D** ("marginal productivity") is a *what-if simulation*; the validator computes a
  representative makespan-reduction figure to prove the inputs exist, not a production formula.
- Dataset scale is "demo-realistic" (single-digit-to-low-tens rows per table) — enough for every chart to
  render with multiple categories/series, not a load test.
