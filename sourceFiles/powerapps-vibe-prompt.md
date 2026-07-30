---
title: "vibe.powerapps Prompt — EDQMS Prototype"
purpose: "Ready-to-use Copilot prompt for generating the EDQMS MVP as a Model-Driven App in Power Apps with Dataverse"
scope: "MVP prototype — 14 entities. Excludes Phase 3 (Risk, Source, Requirement, Payload, Trigger)."
---

# vibe.powerapps — EDQMS Prototype Prompt

Copy the block below (max 4000 characters) and paste into vibe.powerapps. Attach the reference files listed at the end before submitting.

---

## PROMPT (copy from here)

Build a Model-Driven App in Power Apps (Dataverse): **EDQMS Prototype** — ISO 9001:2015 quality chain: Event→Process→Activity→Procedure→Operation/Action/Handout.

**SOLUTION**
Publisher prefix: edqms. Solution: EDQMSPrototype v1.0.0.0.

**STRUCTURAL TABLES (create first)**
Region — primary: Region Name
Scope — primary: Scope Name; Description(multiline)
Channel — primary: Channel Name; Channel Type(choice: Email,Teams,SharePoint,ERP,Physical,Other; required)
Interface — primary: Interface Name; Interface Type(choice: System,Document,Meeting,Form,Other; required)
Product — primary: Product Name; Description(multiline)
Role — primary: Role Name; Description(multiline)

**OPERATIONAL TABLES (in order)**
1. Event — primary: Event Title; Description(multiline); Event Date(date, required); Event Owner(lookup→systemuser, required)
2. Process — primary: Process Name; Description(multiline); Process Owner(lookup→systemuser, required); Event(lookup→edqms_event, required)
3. Activity — primary: Activity Title; Description(multiline); Process(lookup→edqms_process, required)
4. Procedure — primary: Procedure Number; Procedure Title(text, required); Description(multiline); Activity(lookup→edqms_activity, required); Version(text); Approval Date(date); Approved By(lookup→systemuser)
5. Operation — primary: Operation Name; Description(multiline); Sequence Number(whole number, required); Procedure(lookup→edqms_procedure, required)
6. Action — primary: Action Title; Description(multiline); Action Type(choice: Inspection,Sign-off,Hold Point,Corrective,Preventive; required); Condition(multiline); Responsible(lookup→systemuser); Procedure(lookup→edqms_procedure, required)
7. Handout — primary: Handout Title; Description(multiline); Handout Type(choice: Input,Output; required); Document Reference(text); Procedure(lookup→edqms_procedure, required); Interface(lookup→edqms_interface); Channel(lookup→edqms_channel)
8. Constrain — primary: Constrain Title; Description(multiline); Constrain Type(choice: Regulatory,Contractual,Technical; required); Scope(lookup→edqms_scope); Region(lookup→edqms_region); Product(lookup→edqms_product); Operation(lookup→edqms_operation)

**N:N RELATIONSHIPS**
Procedure↔Scope, Procedure↔Region, Procedure↔Product, Procedure↔Role, Activity↔Channel, Activity↔Interface

**APP NAVIGATION**
Area 1 Events: Event
Area 2 Operational Chain: Process, Activity, Procedure
Area 3 Execution: Operation, Action, Handout
Area 4 Configuration: Constrain, Channel, Interface, Role, Scope, Region, Product

**PROCEDURE FORM (central entity)**
Section 1 Identification: Procedure Number, Procedure Title, Activity, Description
Section 2 Approval: Version, Approval Date, Approved By
Tab "Execution Details": subgrids Operations(1:N), Actions(1:N), Handouts(1:N)
Tab "Applicability": subgrids Scopes(N:N), Regions(N:N), Products(N:N)

**EVENT FORM**
Fields: Event Title, Description, Event Date, Event Owner
Subgrid at bottom: Processes(1:N)

**VIEWS — Active Records**
Event: Event Title, Event Date, Event Owner — sort Event Date desc
Process: Process Name, Event, Process Owner — sort Process NameActivity: Activity Title, Process — sort Activity TitleProcedure: Procedure Number, Procedure Title, Activity, Version, Approved By — sort Procedure NumberOperation: Operation Name, Sequence Number, Procedure — sort Sequence NumberAction: Action Title, Action Type, Procedure — sort Action TitleHandout: Handout Title, Handout Type, Procedure, Channel — sort Handout TitleConstrain: Constrain Title, Constrain Type, Scope, Region — sort Constrain Title
**REFERENCE DATA (populate before testing)**
Regions: EMEA, Americas, APAC
Scopes: Offer Process
Products: Power Transformer Repair, On-site Service
Channels: Teams, SharePoint, SAP, Email
Interfaces: SAP-PM, Engineering Portal, BU Interface
Roles: Offer Engineer, FIA Specialist, Project Manager, Quality Manager

## END OF PROMPT

---

## Reference Files to Attach

| File | Path |
|---|---|
| Power Apps Implementation Guide | `site-stakeholder/docs/prototype/power-apps-guide.md` |
| Data Model Documentation | `site-stakeholder/docs/prototype/data-model.md` |
| Data Model Design Rationale | `sourceFiles/EDQMS-01_DataModel_DesignRationale.md` |

> Do **not** attach `broker_interface.md` — it covers Phase 3 mechanisms out of scope for this MVP.
