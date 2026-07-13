# Claude Design Prompt — Global Engineering Portal Prototype Update

## How to use this file
1. Open **Claude Design** and start a new project.
2. Upload `GlobalEngineeringPortal_dahsboard.html` as the existing prototype.
3. Paste the contents of this file as your first message.
4. Claude Design will apply the changes described below module by module.

**Recommended model:** Claude Opus 4.8

---

## Your Task

You are updating an existing dashboard prototype for the **Global Engineering Portal** — an ISO 9001:2015-aligned Quality Management System. The attached HTML file is the current prototype.

Apply every change listed below. Do **not** change the following:
- Color palette: `#00e096` (green accent), `#f2f4f6` (page background), `#ffffff` (panels)
- Sidebar navigation layout and 220px width
- Top bar structure
- Font stack: `-apple-system, BlinkMacSystemFont, sans-serif`
- Panel border radius (`6px`), shadow (`0 1px 4px rgba(0,0,0,0.12)`), and spacing

---

## Global UI Rules

Apply these rules universally across all modules before making any per-tab changes.

**Rule 1 — Mandatory entity table.**
Every tab must always display a primary data table listing all records of that tab's entity (e.g., the Scopes tab shows the Scopes table). Report widgets show only charts — never duplicate the entity table as a report.

**Rule 2 — Rollup columns.**
Wherever a rollup relationship exists (a child table references a parent via FK), add a collapsible/expandable row section in the parent table showing the list of linked child records. Use a chevron toggle. Default state: collapsed.

**Rule 3 — Mirror field styling.**
Fields that are auto-populated from related records (mirror fields) must be visually distinct from user-editable fields: use a slightly grey background (`#f7f8f9`) and an italic label. They should be read-only — no user input allowed.

**Rule 4 — Control module is read-only.**
The tabs Capacity, Usage, and Productivity in the Control module have **no create/edit forms**. Remove any "New record" or "Edit" buttons from those tabs. They display only filtered query results and chart widgets.

---

## Module: Customers

### Forecasts tab

**Form changes:**
- The `forecastPeriod` field (enum: Annual / Quarter / Month) controls which other period fields are visible. Implement conditional field visibility:
  - When `forecastPeriod = Month`: show `forecastMonth` (year + month picker). `periodStart` and `periodFinish` are auto-set to that month (read-only).
  - When `forecastPeriod = Quarter`: show `forecastQuarter` (year + quarter selector). `periodStart` is a user date input (month + year). `periodFinish` is auto-calculated as `periodStart + 4 months` (read-only).
  - When `forecastPeriod = Annual`: show `forecastYear`. `periodStart` and `periodFinish` are both user date inputs (month + year).
- Hide fields that don't apply to the selected period type.
- `totalEstimatedHours` is read-only computed.

**Reports:**
- Keep Report-A (line chart: totalEstimatedHours by period, one series per factory).
- **Remove Report-B widget entirely.**

---

### Forecast Scopes tab

**Form changes:**
- Remove the `estimatedCost` field from the form.
- `processID`, `roles`, and `estimatedHours` are read-only computed (apply mirror field styling).

---

## Module: Operation

### Tasks tab

**Tab label:** Rename to **"Task Templates"**. Add a subtitle or description beneath the tab header: *"Tasks are templates for execution. Jobs are created from tasks in the Workload module."*

**Form changes — cascading selector chain:**
The form must implement a 4-step cascading selection:
1. **Event** (user selects from Events table) → filters the Process options
2. **Process** (options filtered to processes triggered by the selected event) → filters Workflow options
3. **Workflow** (options filtered to workflows matching the selected process) → auto-populates Activity
4. **Activity** (auto-set from selected Workflow — read-only mirror field)

`taskName` is read-only computed: `CONCAT(actionName, ' — ', activityName, ' — ', processName)`.
`roles` is read-only computed (from Competence via taskID).
`products` and `scopes` are read-only computed (from Activity Payload).

**Planning filter bar:**
Above the entity table, add a persistent filter bar with 5 fields (for planners to find relevant tasks):
- Scope Name
- Design Type
- Product Name
- Event Name
- Process Name

**Reports:**
- Keep Report-A (bar: count of tasks grouped by processID).
- **Replace Report-B** with a bar chart titled "Top 10 Execution Gaps". Shows the 10 task/job pairs with the largest difference between `executionTime` (planned) and `realExecutionTime` (actual from Jobs), sorted ascending by gap (largest overrun first). Filters: processName, roles, productName, scopeName.

---

### Events tab

**Concept label:** Add a description beneath the tab header: *"An Event is an aggregator of processes — it triggers execution but is not executed itself."*

**Table changes:**
Add 3 collapsible rollup sections in each event row:
- **Processes** — list of processes triggered by this event
- **Tasks** — list of task templates for each triggered process
- **Open Tickets** — count and list of open tickets linked to this event

Add mirror fields (read-only) to the table columns:
- `factoryName` (from ticketID rollup)
- `productName` (from ticketID rollup)
- `scopeName` (from ticketID rollup)

**Reports:**
- **Remove both existing report widgets.**
- Add a single **Report-A**: Bar chart titled "Open Tickets by Event". Shows open ticket count grouped by `eventName`, with separate bars or series per factory. Filters: factoryName (default: All), productName (default: All), scopeName (default: All).

---

### Processes tab

**Form changes:**
- Add optional text field `processSystemID` (label: "External System ID", placeholder: "e.g. SAP-0042 — optional").
- Make `targetExecutionTime` read-only with mirror field styling. Add a tooltip: "Average execution time derived from task groups sharing the same action + workflow combination."
- `activities` and `tasks` show as collapsible rollup sections.

Add mirror columns to the table (read-only): `productName`, `scopeName`, `design` — derived from the tasks rollup.

**Reports:**
- **Replace Report-A filters** with: productName (default: All), scopeName (default: All), design (default: All). Keep the bar chart rule (count of tasks grouped by processName).
- **Remove Report-B widget entirely.**

---

### Activities tab

**Form changes — simplify:**
- Remove these fields from the form: `executionTime`, `owner`, `status`, `startDate`, `endDate` (execution belongs to Tasks, not Activities).
- `roleID` is read-only (derived from linked Tasks). Apply mirror field styling with label "Role (derived from tasks)".
- `procedureID` becomes an **attachment widget** with two sub-fields:
  - URL field (label: "Procedure Link")
  - Text field (label: "Procedure ID / Description")

**Reports:** Remove all report widgets. This tab shows the entity table only.

---

### Workflows tab

**Form changes:**
- `workflowName` is auto-generated read-only: `CONCAT(activityName, ' — ', processName)`. Apply mirror field styling with label "Workflow Name (auto-generated)".
- `activities` selector: change from multi-select to **single-select** dropdown.
- Show the following as collapsible read-only sections (mirror columns populated from the linked taskID rollup):
  - Inputs
  - Outputs
  - Scopes
  - Customer
  - Procedures
  - Products
  - Constraints

**Reports:** Remove all report widgets. Entity table only.

---

### Actions tab

**Filter bar additions:**
Above the entity table, add two filter fields to help users find actions by context:
- "Filter by Workflow" (activity + process combination)
- "Filter by Activity"

**Table additions:**
- `taskID` rollup column: collapsible list of tasks using this action.
- `activityID` mirror column: read-only, derived from taskID rollup.
- `workflowID` mirror column: read-only, derived from taskID rollup (enables workflow-based filtering).

**Reports:** Remove all report widgets. Entity table only.

---

### Constraints tab

**Reports:** Remove all report widgets. Entity table only (lookup/master data).

---

### Handouts tab

**Form changes:**
- Add **Template attachment widget**: file upload field with an associated text input for the attachment title. Label: "Template".
- Add `type` field: single-select dropdown with options `data` / `file`.
- **Remove** `activityID` field.
- **Remove** `fileURL` field.
- Add `taskID` rollup section (collapsible list of tasks that reference this handout).

**Reports:** Remove all report widgets. Entity table only.

---

### Channels tab

**Form changes:**
- **Remove** `channelDescription` field.
- **Remove** `events` field.
- **Remove** `channelType` field.
- `channelOwner`: change to a plain text input (not a FK dropdown). Add tooltip: "Name of the company or person responsible for managing this channel."

**Reports:** Remove all report widgets. Entity table only.

---

## Module: Inventory

### Product Scopes tab

**Form changes:**
- `businessSegment`: change to read-only mirror field (derived from linked Product Group). Apply mirror field styling.
- `productClassID`: change to read-only mirror field (derived from linked Product Group). Apply mirror field styling.
- Add `constraintName` as a collapsible rollup section, grouped by constraint type.
- **Remove** `ratings` field.
- **Remove** `design` field.

**Reports:** Remove all report widgets. Entity table only.

---

### Product Groups tab

**Form changes:**
- **Remove** `groupCode` field.
- **Remove** `groupName` field.
- `products`: change from multi-select to **single-select**.
- `productClassID`: change to **multi-valued** (multi-select or tag list).

**Reports:** Remove all report widgets. Entity table only.

---

### Scopes, Products, Product Class tabs

**Reports:** Remove all report widgets. Entity tables only (master data).

---

## Module: Workload

### Tickets tab

**Form changes:**
- Add `eventID` field: FK dropdown (label: "Event", options from Events table).
- `forecastScopeID`: update display to show a concatenated string: `scopeName — businessSegment — productClassID — productName`. Change to a rollup selector filtered by `customerName` and `eventID`.
- Make the following read-only mirror fields (derived from the selected Forecast Scope):
  - `processID` (label: "Process")
  - `products` (label: "Products")
  - `scopes` (label: "Scopes")
  - `constraintName` (label: "Constraints")
- Add `targetDate` field: datetime input (label: "Target Resolution Date").
- `resolutionTime`: change to datetime input (label: "Planned Delivery Date").
- Add `taskID` collapsible rollup section: shows tasks matching this ticket's scope, product, and customer.
- **Remove** `design` field.
- **Remove** `seBuilder` field.
- **Remove** `ticketPriority` field.

**Reports:**
- Keep Report-A (bar: count of tickets by customerName; filters: ticketStatus, processID, period, priority).
- **Replace Report-B** with a donut chart: ticket count grouped by `scopeName`. Filters: customerName, period, constraintName.

---

### Projects tab

**Form changes:**
- Add `projectName` text input (label: "Project Name").
- Add `clientName` text input (label: "External Client Name").
- Add `estimatedTime` read-only computed field: sum of task executionTime grouped by ticketID.
- Add `executionTime` read-only computed field: sum of job realExecutionTime grouped by ticketID.
- Add `jobID` read-only mirror field (derived from Tickets rollup).

**Reports:**
- **Replace Report-A** with a grouped bar chart titled "Estimated vs. Real Execution". Shows estimated time (from tasks) and real time (from jobs) side by side for each project. Filters: customerName, projectStatus.
- **Remove Report-B widget.**

---

### Jobs tab

**Form redesign — planning workflow:**
Restructure the create/edit form as a sequential planning workflow with 4 steps:

**Step 1 — Select template:**
- `taskID`: dropdown to select a Task Template (label: "Task Template"). Shows taskName.

**Step 2 — Schedule:**
- `startDate`: datetime input (label: "Planned Start Date").
- `endDate`: datetime input (label: "Planned End Date").

**Step 3 — Assign:**
- `userID`: FK dropdown (label: "Assignee"). **Important:** filter this dropdown to show only People whose roleID matches the roleID of the selected task template.
- `roleID`: read-only mirror field (auto-populated from selected userID).
- `squadName`: read-only computed field (auto-populated from selected person's squad).

**Step 4 — Dependencies (optional):**
- `predecessorJob`: dropdown (label: "Predecessor Job"). Options show `CONCAT(projectName, ' — ', jobName)`.
- `dependencyType`: single-select dropdown with options: Start-to-Start / Start-to-Finish / Finish-to-Finish / Finish-to-Start.

**Additional fields:**
- `realStartDate`: datetime input (label: "Actual Start Date").
- `realEndDate`: datetime input (label: "Actual End Date").
- `realExecutionTime`: read-only computed (realEndDate − realStartDate, displayed in hours).
- `customerName`: read-only computed (from projectID via ticketID).
- `jobStatus`: enum dropdown (Queued / Active / Done / Stopped).

**Reports:**
- Keep Report-A (line chart: count of jobs reaching Done status per week; filters: roleID, period).
- Keep Report-B (bar chart: SUM(realExecutionTime) grouped by roleID; filters: jobStatus, ticketID, period).

---

## Module: Control

> All tabs in this module are **read-only**. Remove all create/edit/delete buttons and forms. These tabs query and aggregate data from other modules.

### Capacity tab

**Attribute/filter changes:**
- Remove all create/edit forms.
- Add `periodStart` and `periodFinish` date-range pickers at the top of the tab as primary report-period selectors (month + year format).
- `allocatedHours`: computed from executionTime of Tasks linked to forecastScopes per period (read-only).
- `availableHours`: total available hours for the selected roleID in the selected period (read-only).

**Reports:**
- Keep Report-A: dual bar chart (availableHours vs. allocatedHours side by side, grouped by roleName). Filters: periodStart, periodFinish, eventTitle, factoryID, roleID, functionName.
- Keep Report-B: bar chart (utilization % grouped by functionName). Filters: period, factoryID, roleID, functionName.

---

### Usage tab

**Attribute/filter changes:**
- Remove all create/edit forms.
- All data in this tab is sourced from the **Jobs** table (not Tasks or Forecasts).

**Reports:**
- Keep Report-A: line chart (usedHours plotted by period, one series per functionName). Filters: customerName, functionName, period, squadName.
- Keep Report-B: heatmap (rows = role names, colour intensity = number of allocated jobs). Filters: customerName, functionName, period, squadName.

---

### Productivity tab

**Attribute/filter changes:**
- Remove all create/edit forms.

**Reports:**
- Keep Report-A: donut chart (count of teams grouped by efficiency bucket: <80% / 80–100% / >100%). Filters: functionID, factoryID, period.
- **Remove Report-B widget.**
- **Add Report-C**: bar chart titled "Oversized Tasks". Shows count of tasks that could be performed by less-experienced resources (based on `levelRank`). Filter: processName.
- **Add Report-D**: bar chart titled "Marginal Productivity". What-if analysis showing estimated time/throughput gain when adding extra headcount of a given role to a process or event. Filters: processName, eventName, roleName, plus a numeric spinner input "Extra Headcount" (default: 1, min: 1, max: 20) that recalculates the chart live.

---

## Module: Talent

### Add new tab: Squads

Insert a new tab **"Squads"** in the Talent module, positioned after Roles.

**Entity table columns:** squadID, squadName, squadType, managerName, managerEmail.

**Create/edit form fields:**
- `squadName`: text input.
- `squadType`: single-select dropdown (Outsource / Internal).
- `managerName`: text input.
- `managerEmail`: email input.

Add a collapsible `people` rollup section in each squad row showing linked People.

**Reports:** No report widgets. Entity table only.

---

### Roles tab

**Form changes:**
- Add `overheadCost` read-only computed field (label: "Avg. Overhead Cost", tooltip: "Average personalCost of people in this role"). Apply mirror field styling.
- Add `taskName` collapsible rollup section showing tasks that require this role.
- **Remove** `departmentID` field.

**Reports:**
- Keep Report-A: donut chart (sum of quantity grouped by functionID). Filters: functionID, skillLevelID, isActive.
- **Replace Report-B** (or add if absent) with a donut chart titled "Tasks by Role". Shows count of tasks grouped by roleName, only for roles where headCount > 0. Filter: levelName.

---

### People tab

**Form changes:**
- Add `personalCost` numeric decimal input (label: "Personal Cost").
- Add `squadID` FK dropdown (label: "Squad", options from Squads table).
- Add `onboardID` read-only link field (label: "Onboarding Record", links to the person's Onboarding entry if it exists). Apply mirror field styling.

**Reports:** Keep Report-A (bar: count of active People grouped by functionID; filters: departmentID, locationID, isActive).

---

### Add new tab: Onboarding

Insert a new tab **"Onboarding"** in the Talent module, positioned last.

**Entity table columns:** userID (shows userName), functionID, roleID, isCertified, certifications.

**Create/edit form — certification checklist layout:**

1. `userID`: FK dropdown (label: "Person"). On selection, auto-populate `functionID` (read-only, mirror).
2. Roles section: collapsible list of roles associated with the selected person's function (rollup from Roles via functionID).
3. Competences section: for each role, show a nested list of competences (from Competence via roleID). Each competence row shows:
   - competenceName (read-only)
   - scopeName (read-only, computed)
   - productName (read-only, computed)
   - resources (read-only, computed)
   - constraintName (read-only, computed — grouped by constrainTypeName)
   - `isCertified` toggle (checkbox, user-editable)
4. `certifications`: free-text field (label: "Certification Numbers / Dates").

**Reports:** No report widgets. Entity table only.

---

## New Module: Quality

Add **"Quality"** as the 7th module in the sidebar navigation (after Talent). Use the same green sidebar entry style as existing modules.

The Quality module contains 6 tabs:

---

### Risks tab

**Entity table columns:** riskID, riskTitle, riskCategory, riskSeverity, riskLikelihood, riskPriorityNumber, riskStatus, riskOwner.

**Create/edit form fields:** riskTitle, riskDescription, riskCategory (enum: Threat / Opportunity), riskSeverity (integer 1–5 slider or stepper), riskLikelihood (integer 1–5 slider or stepper), `riskPriorityNumber` (read-only computed: severity × likelihood), riskOwner (FK → People), riskStatus (enum: Open / UnderTreatment / Closed / Accepted), `eventID` FK dropdown (optional), `requirementID` FK dropdown (optional).

Add `actions` collapsible rollup section.

**Reports:**
- **Report-A**: Scatter plot (X-axis = riskLikelihood, Y-axis = riskSeverity). Each bubble represents a risk; bubble size = riskPriorityNumber; bubble color = riskCategory (Threat = red, Opportunity = green). Draw quadrant divider lines at x=3, y=3. Filters: riskCategory, riskStatus, owner, period.
- **Report-B**: Table — Open Risk Register. Rows: risks where riskStatus IN (Open, UnderTreatment). Columns: title, category, severity, likelihood, RPN, owner, status, linked action count, last reviewed date. Filters: riskCategory, riskStatus, owner.

---

### Sources tab

**Entity table columns:** sourceID, sourceName, sourceCategoryID, sourceOwner, isActive.

**Create/edit form fields:** sourceName, sourceCategoryID (FK → Source Categories), sourceOwner (FK → People), sourceDescription, isActive toggle.

Add collapsible rollup sections: `events` (linked events) and `requirements` (linked requirements).

**Reports:**
- **Report-A**: Bar chart (count of linked Events grouped by sourceCategoryID). Filters: sourceCategoryID, period, isActive.
- **Report-B**: Table — Source → Event → Risk Traceability. Columns: source name, category, event count, risk count, open risk count. Filters: sourceCategoryID, isActive.

---

### Source Categories tab

**Entity table columns:** sourceCategoryID, sourceCategoryName, sourceCategoryDescription.

**Reports:** No report widgets. Entity table only (lookup).

---

### Requirements tab

**Entity table columns:** requirementID, requirementName, requirementType, sourceID, isActive.

**Create/edit form fields:** requirementName, requirementDescription, sourceID (FK → Sources), requirementType (enum: Customer / Statutory / Regulatory / Internal), isActive toggle, productID (FK → Products, optional).

Add `risks` collapsible rollup section.

**Reports:**
- **Report-A**: Donut chart (count of requirements grouped by requirementType). Filters: sourceID, isActive, productID.
- **Report-B**: Table — Requirement-to-Risk Compliance. Columns: requirement name, type, source, linked risk count, open risk count, highest RPN. Filters: requirementType, sourceID, isActive.

---

### actionApplication tab

**Entity table columns:** applicationID, applicationName, isoClause.

**Reports:** No report widgets. Entity table only (lookup).

---

### Event Log tab

**Entity table columns:** logID, eventID, previousStatus, newStatus, changedAt, changedBy.

**Note:** This tab is read-only — records are system-generated. Remove create/edit forms.

**Reports:**
- **Report-A**: Bar chart — Event Resolution Time Distribution. Shows count of resolved events grouped by resolution time bucket: <1h / 1–8h / 8–24h / 1–7d / >7d. Filters: period, owner, priority.
- **Report-B**: Table — Event Audit Trail. Shows full state-change history. Columns: previous status, new status, changed by, changed at, note. Filters: eventID, changedBy, period.

---

## UI Patterns Reference

When implementing the changes above, use these reusable patterns consistently:

**Cascading dropdowns:** Each selector clears and re-fetches options when its parent changes. Show a loading indicator while options load. If no options are available (e.g., no processes for a given event), show a disabled greyed-out state with the message "No options for selected [parent]."

**Conditional field groups:** Use smooth show/hide transitions (CSS `max-height` transition or fade). Hidden fields are excluded from form validation. Always show a brief inline label explaining why a field is hidden (e.g., "forecastQuarter only shown when Period = Quarter").

**Attachment widget:** Render as a card with a dashed-border upload zone on the left and a text input on the right. Show filename and file size after upload. Allow remove/replace. For link-type attachments (procedures), swap file upload for URL input.

**Rollup rows:** Use a chevron `›` / `˅` toggle at the left of the row. Expanded state shows an indented sub-table or list of linked records with key columns. Add a row count badge next to the chevron, e.g. `3 tasks`.

**Mirror field styling:** Background `#f7f8f9`, border `1px solid #e3e6e8`, label in italic, small lock icon `🔒` or "Auto" badge to signal read-only. Never show these fields in an editable form state.

**What-if inputs (Report-D):** Numeric stepper input in the filter bar with +/− buttons and direct text entry. On change, trigger immediate chart recalculation. Show a subtle "Simulated" watermark on the chart to distinguish from real data.
