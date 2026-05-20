# EDQMS-01 — Event Driven Quality Management System
## Data Model Design Rationale

**Diagram:** [EDBPM — EDQMS ER-UML](https://lucid.app/lucidchart/090097f0-5c82-40ac-999b-ff1c96ba5c94/edit) (Tab: EDQMS ER-UML)
**Reference Sources:** ISO/FDIS 9001:2015(E) · Cochran, C. (2015). *ISO 9001:2015 in Plain English*. Paton Professional.

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Project Goal: Event-Driven Quality Management](#2-project-goal-event-driven-quality-management)
3. [Architecture Overview: Key Entity Groups](#3-architecture-overview-key-entity-groups)
4. [The Risk Entity: Design Rationale Against ISO 9001:2015 §6.1](#4-the-risk-entity-design-rationale-against-iso-90012015-61)
5. [The actionApplication Entity](#5-the-actionapplication-entity)
6. [Full ISO 9001:2015 Clause Mapping](#6-full-iso-90012015-clause-mapping)
7. [PDCA Cycle Integration](#7-pdca-cycle-integration)
8. [Open Design Items and Recommendations](#8-open-design-items-and-recommendations)
9. [Conclusion](#9-conclusion)
10. [References](#references)

---

## 1. Purpose and Scope

This document describes how the entity-relationship data model defined in the **EDQMS ER-UML** diagram supports the goals of project **EDQMS-01**: the design of an Event Driven Quality Management System (EDQMS) that is fully aligned with ISO 9001:2015.

The model is grounded in two authoritative sources:

- **ISO 9001:2015** (`ISO90012015_EN_ocr.pdf`) — the normative standard, which defines all "shall" requirements.
- **Cochran (2015)** (`iso-9001-2015-in-plain-english_Craig-Cochran_.md`) — a practitioner interpretation that clarifies implementation intent, including the Risk Priority Number (RPN) methodology, the connection between clause 4.1/4.2 context analysis and risk identification, and practical guidance for integrating risk-based thinking into QMS processes.

---

## 2. Project Goal: Event-Driven Quality Management

The central thesis of EDQMS-01 is that quality management should be **reactive and proactive at the same time** — driven by Events that occur within business operations rather than by periodic, calendar-based audits alone. This aligns directly with the philosophy expressed in ISO 9001:2015 §0.1:

> *"The adoption of a quality management system is a strategic decision for an organization that can help to improve its overall performance and provide a sound basis for sustainable development initiatives."*
> — ISO 9001:2015, §0.1

Cochran reinforces that QMS processes must be the true business processes of the organisation — not a parallel structure maintained for certification:

> *"QMS processes are the way that we should holistically manage our organisations, and they must be fully incorporated into our business processes."*
> — Cochran (2015), Chapter 3

In the EDQMS data model, the **Event entity is the architectural pivot**: it connects all operational entities (Process, Activity, Product, Source, Requirement) to the quality management chain (Risk, Action, Procedure). Quality is not an overlay — it is embedded in the event stream of daily operations.

---

## 3. Architecture Overview: Key Entity Groups

The data model is organised into five functional groups, each addressing specific clauses of ISO 9001:2015.

### 3.1 Organisational Context (Clauses 4.1–4.3)

**Entities:** Source, Source Category, Requirement, Scope, Scope Category, Constrain, Constrain Type, Region, Location, Business Unit, Department.

These entities collectively represent the organisation's internal and external context. ISO 9001:2015 §4.1 requires the organisation to determine issues that affect its strategic direction, while §4.2 requires identification of interested party requirements. In the EDQMS model:

- **Source / Source Category** capture external and internal issue origins.
- **Requirement** captures interested party obligations (customer, statutory, regulatory).
- **Scope / Scope Category** establish the applicability boundaries of the QMS.
- **Constrain / Constrain Type** encode the regulatory and contractual limits that bound risk treatment options.

Cochran identifies the output of clauses 4.1 and 4.2 as the primary raw material for risk identification:

> *"Each requirement [of an interested party] may constitute a risk, an opportunity, or a combination of both."*
> — Cochran (2015), Chapter 4

---

### 3.2 Operations Chain (Clause 4.4 — QMS Processes)

**Entities:** Process, Activity, Procedure, Operation, Action, Handout, Tool, Interface, Channel, Property, Specs, Product, Product Category.

ISO 9001:2015 §4.4.1 requires the organisation to establish, implement, maintain, and continually improve a QMS including all needed processes and their interactions. The model reflects this hierarchy explicitly:

| Entity | Role in the Model |
|---|---|
| **Process** | Top-level business activity container (processID, processName, processOwner, processDescription). |
| **Activity** | Sub-process within Process (activityID, activityTitle, activityDescription, processName). |
| **Procedure** | Documented method for executing an Activity (procedureID, procedureNumber as external reference). |
| **Operation** | Specific operational steps within a Procedure (operationID, operationName, operationOwner). |
| **Action** | A discrete quality management intervention (see Section 5). |

The **`is subprocess`** relationship enables self-referential Process decomposition, supporting hierarchical process models as required by §4.4.1(b) (sequence and interaction of processes).

Cochran's description of a complete process model maps directly onto this entity chain:

> *"Criteria and methods... Resources... Responsibility and authority... Risks and opportunities... Evaluation... Improvement."*
> — Cochran (2015), Chapter 2 (on clause 4.4)

---

### 3.3 Leadership and Resource Context (Clause 5)

**Entities:** User, Role.

Every owner attribute in the model — `processOwner:userName`, `eventOwner:UserID`, `riskOwner:userName`, `operationOwner:userName`, `channelOwner:UserName`, `sourceOwner:userName`, `regionOwner:userName` — is typed as a foreign key reference to the **User** or **Role** entities.

This design enforces accountability at every node of the quality management chain, in compliance with:

- ISO 9001:2015 **§5.3** — Organisational roles, responsibilities, and authorities.
- ISO 9001:2015 **§6.2.2(c)** — When planning how to achieve objectives: *"who will be responsible."*

---

### 3.4 Risk Management (Clause 6.1) — New in this Revision

**Entities:** Risk, `<enumeration> riskCategory`.

This is the most significant addition in the current model revision. It is addressed in full detail in [Section 4](#4-the-risk-entity-design-rationale-against-iso-90012015-61).

---

### 3.5 Event Engine — The Architectural Core

**Entity:** Event (EventID, eventTitle, eventOwner:UserID, Description).

The Event entity is the central driver of the EDQMS architecture. Its attributes are deliberately minimal, allowing Events to be lightweight triggers. Its relationships span the entire model:

- `Event` **triggers** `Process` — connects operational execution to quality oversight.
- `Event` **triggers** `Risk` — detects or confirms risk conditions in real time.
- `Event` **applies to** `Source` — links events to their origin context.
- `Event` **applies to** `Product` — connects quality events to affected products.
- `Event` **requires** `Activity` — defines which activities are initiated by an event.

This pattern implements the ISO 9001:2015 process model's feedback loops at the data architecture level — monitoring checkpoints that detect deviations and trigger corrective or preventive responses (see ISO 9001:2015, Figure 1 — schematic representation of the elements of a single process).

---

## 4. The Risk Entity: Design Rationale Against ISO 9001:2015 §6.1

The Risk entity was introduced based on the requirements of ISO 9001:2015 Clause 6.1 and the practitioner guidance of Cochran (2015).

### Risk Entity Attributes

```
riskID            (PK — black fill in diagram)
riskTitle
riskDescription
riskCategory      (FK → <enumeration>: Threat | Opportunity)
riskPriorityNumber
riskOwner         :userName (FK → User)
```

---

### 4.1 The riskCategory Enumeration: Threat | Opportunity

ISO 9001:2015 is explicit that "risk" encompasses both positive and negative deviations:

> *"Risk is the effect of uncertainty and any such uncertainty can have positive or negative effects. A positive deviation arising from a risk can provide an opportunity, but not all positive effects of risk result in opportunities."*
> — ISO 9001:2015, §0.3.3

The `riskCategory` enumeration (`Threat | Opportunity`) directly operationalises this. A **Threat** record represents a negative-effect risk requiring mitigation; an **Opportunity** record represents a favourable situation that the organisation should plan to exploit.

This dual encoding prevents the common implementation error of treating risk management as purely defensive — which would cause the EDQMS to miss the innovation and improvement signals that ISO 9001:2015 §6.1.1 explicitly requires to be captured.

---

### 4.2 The riskPriorityNumber Attribute

ISO 9001:2015 §6.1.1 requires the organisation to *"determine the risks and opportunities that need to be addressed"* — implying a selection and prioritisation mechanism. Cochran describes the standard approach:

> *"The two rating factors (severity and likelihood) are multiplied to give you a risk priority number (RPN). Once you have rated the risks and opportunities and calculated the RPN for each one, select a threshold for action."*
> — Cochran (2015), Chapter 4

The `riskPriorityNumber` attribute encodes this calculated value, enabling the EDQMS to apply a threshold filter to determine which risks advance to the Action planning stage. This directly supports the proportionality requirement:

> *"Actions taken to address risks and opportunities shall be proportionate to the potential impact on the conformity of products and services."*
> — ISO 9001:2015, §6.1.2

---

### 4.3 Risk ↔ Event: The Primary Event-Driven Relationship

The **`Trigger`** relationship between Event and Risk is the defining architectural decision of the EDQMS. In a traditional, document-centric QMS, risks are identified in scheduled review meetings. In an event-driven architecture, quality events from daily operations directly surface risk conditions in near-real time.

**Event → Risk trigger examples:**

| Event (eventTitle) | Risk Triggered | riskCategory |
|---|---|---|
| "Product defect reported by customer" | Product conformity risk | Threat |
| "Supplier delivery deviation" | Supply chain risk | Threat |
| "Audit finding — process deviation" | Process compliance risk | Threat |
| "New market entry signal detected" | Market expansion opportunity | Opportunity |
| "Regulatory change notification" | Compliance risk | Threat |

**Reverse path — Risk → Event:** A recorded Risk can schedule monitoring Events to detect whether the risk condition is materialising, before it becomes a nonconformity. This proactive surveillance loop is the event-driven implementation of ISO 9001:2015's preventive intent:

> *"One of the key purposes of a quality management system is to act as a preventive tool. Consequently, this International Standard does not have a separate clause or subclause on preventive action. The concept of preventive action is expressed through the use of risk-based thinking."*
> — ISO 9001:2015, §A.4

> **NOTE:** ISO 9001:2015 §A.4 states that risk-based thinking "represents the application of risk-based thinking to planning and implementing quality management system processes." The `Event ↔ Risk` Trigger relationship is the data-model implementation of this requirement.

---

### 4.4 Risk ↔ Requirement (Apply to)

Risks are contextualised against Requirement records in the model. This relationship implements ISO 9001:2015 §6.1.1(a), which states that risks must be addressed to *"give assurance that the quality management system can achieve its intended result(s)."*

Intended results are defined by Requirements — customer specifications, regulatory mandates, statutory obligations. When a Risk is linked to a Requirement, the system can evaluate which specific obligations are threatened, enabling targeted and auditable risk responses.

Cochran identifies Requirements (from clauses 4.1 and 4.2) as the primary raw material for risk identification:

> *"Each requirement [of an interested party] may constitute a risk, an opportunity, or a combination of both. There is a third input to your risks and opportunities: corrective actions. Corrective actions are aimed at removing causes of nonconformity and ultimately removing risk."*
> — Cochran (2015), Chapter 4

---

## 5. The actionApplication Entity

**Entities:** actionApplication (actionApplicationID, actionApplicationName, actionApplicationDescription).

ISO 9001:2015 §6.1.2(b)(1) specifies that the organisation must plan how to *"integrate and implement the actions into its quality management system processes."* The `actionApplication` entity fulfils this requirement by classifying Actions according to their QMS process context.

The Note embedded in the diagram defines the intended application types:

| actionApplicationName | QMS Clause | Description |
|---|---|---|
| Risk management | 6.1.2 | Actions specifically designed to treat or exploit identified risks. |
| Control | 8 | Actions that maintain process parameters within specified limits. |
| Communication | 7.4 | Actions that disseminate quality information to relevant parties. |
| Monitoring | 9.1 | Actions that observe and measure process performance. |
| Improvement | 10 | Actions that enhance process effectiveness (correction, corrective action, continual improvement). |

The **`Action —[belong to]→ actionApplication`** relationship provides:

1. **Clause-level traceability:** Every Action maps to the QMS process domain it serves.
2. **Structured management review inputs:** ISO 9001:2015 §9.3.2(e) requires review of *"the effectiveness of actions taken to address risks and opportunities"* — actionApplication enables filtering by category.
3. **Integration proof:** Demonstrates to auditors that actions are integrated into QMS processes, not managed ad hoc.

Cochran's three requirements for risk actions align directly with the entity design:

> *"They are planned... They are integrated into QMS processes... They must be proportional... They are checked for effectiveness."*
> — Cochran (2015), Chapter 4

> **OPEN ITEM:** A direct many-to-many relationship between `Risk` and `Action` (`Risk —[addressed by]→ Action`) is recommended. Currently the link is mediated through `actionApplication`. A direct relationship would allow the system to query: *"Which actions are treating this specific risk?"* — a key traceability requirement of §6.1.2(a).

---

## 6. Full ISO 9001:2015 Clause Mapping

| Entity / Relationship | ISO 9001:2015 Clause | Requirement Supported |
|---|---|---|
| `Risk.riskCategory` (Threat \| Opportunity) | 0.3.3 & 6.1.1 | Dual nature of risk: threats (negative effects) and opportunities (positive deviations) must both be determined and addressed. |
| `Risk ↔ Event` (Trigger) | 6.1.1 (a–d) | Events detect or confirm risks. The QMS must give assurance of achieving results; Events in the EDQMS are the real-time detection mechanism. |
| `Risk ↔ Requirement` (Apply to) | 6.1.1 (a) | Risks affect the organisation's ability to meet customer, statutory, and regulatory requirements. |
| `Risk.riskPriorityNumber` | 6.1.1 (determine which need to be addressed) | Enables proportionate action: significant risks (above RPN threshold) receive prioritised controls. Implements Cochran's severity × likelihood = RPN methodology. |
| `Action ↔ actionApplication` (belong to) | 6.1.2 (b)(1) | Actions must be integrated into QMS processes. `actionApplication` classifies actions by their QMS context (Risk mgmt, Control, Communication §7.4, Monitoring, Improvement). |
| `Action → Role / Operation / Property` | 6.2.2 (a–c) | When planning how to achieve objectives: what will be done (Operation), who is responsible (Role), what resources are required (Property). |
| `Event ↔ Process` (Trigger) | 4.4.1 (f) | Processes must address risks and opportunities as determined in clause 6.1. Events link process execution to risk detection. |
| `Source ↔ Requirement` (Apply to) | 4.1 & 4.2 | Internal/external issues (Source) and interested party requirements (Requirement) are the primary raw material for risk identification. |
| `Scope & Constrain → Risk` | 4.3 | Risks are bounded by the QMS scope and constrained by regulatory/contractual limits that define the boundaries of applicability. |
| `Product ↔ Risk` | 6.1.2 | Actions addressing risks must be proportionate to potential impact on product and service conformity. |
| `User / Role` ownership on all entities | 5.3, 6.2.2(c) | Accountability and authority are defined for every entity in the model, from Process owner to Risk owner to Action owner. |
| `Process → Activity → Procedure → Operation` | 4.4.1 | QMS processes and their interactions are explicitly modelled at four levels of decomposition. |

---

## 7. PDCA Cycle Integration

ISO 9001:2015 §0.3.2 describes the Plan-Do-Check-Act cycle as applicable to all processes and to the QMS as a whole. The EDQMS data model encodes the PDCA loop at the entity level:

| PDCA Phase | EDQMS Entities | Mechanism | ISO 9001:2015 Ref. |
|---|---|---|---|
| **PLAN** | Risk, Source, Requirement, Scope | Identify threats and opportunities from internal/external context; assign `riskPriorityNumber` to determine significance. | 4.1, 4.2, 6.1.1 |
| **DO** | Action, actionApplication, Role, Operation, Procedure | Plan and implement actions classified by application type. Assign responsible Role and required Operations. | 6.1.2, 6.2.2 |
| **CHECK** | Event (monitoring), Product, Specs | Trigger monitoring Events to compare process outputs against Specs and Requirements; detect new risks. | 9.1, 9.3.2(e) |
| **ACT** | Event (corrective/preventive), Risk (updated RPN), Action | New Events feed back into risk re-assessment; close the PDCA loop through revised `riskPriorityNumber` and updated Actions. | 10.1, 10.2 |

Cochran summarises the risk management steps in a way that maps precisely onto this PDCA flow:

> *"1. Scan the environment and objectively look inward at the organisation. 2. Identify the organisation's risks and opportunities. 3. Determine which risks and opportunities are the most significant. 4. Determine actions to proactively manage the risks and opportunities. 5. Continually evaluate the effectiveness of the actions."*
> — Cochran (2015), Chapter 3

---

## 8. Open Design Items and Recommendations

The following items are recommended for the next iteration of the EDQMS ER-UML diagram.

### 8.1 Direct Risk ↔ Action Relationship *(Priority: High)*

ISO 9001:2015 §6.1.2(a) explicitly requires *"actions to address these risks."* Currently there is no direct relationship between the `Risk` and `Action` entities — the link is mediated through `actionApplication`. Adding `Risk —[addressed by]→ Action` would:

- Complete the core risk treatment traceability chain.
- Enable direct queries: *"Show all Actions treating risks above RPN threshold X."*
- Satisfy auditor requirements for documented evidence linking specific risks to specific actions.

### 8.2 Risk Review / Re-assessment Event *(Priority: Medium)*

ISO 9001:2015 §9.3.2(e) requires management review inputs to include *"the effectiveness of actions taken to address risks and opportunities."* A dedicated `actionApplicationName = 'Risk Review'` event type, or a periodic Event subtype, would create an explicit, scheduled feedback loop that re-evaluates `riskPriorityNumber` after Actions have been implemented.

### 8.3 Nonconformity Entity (Clause 10.2) *(Priority: Medium)*

ISO 9001:2015 §10.2 requires the organisation to react to nonconformities and implement corrective action. A `Nonconformity` entity (linked to Event, Product, Process, and Action) would extend the EDQMS to cover clause 10 requirements and complete the improvement cycle that begins with Risk detection.

### 8.4 Documented Information Entity (Clause 7.5) *(Priority: Low)*

Cochran notes:

> *"Smart organisations will document their process for determining and rating risks and opportunities, and they will keep records of what they learn."*
> — Cochran (2015), Chapter 4

A `DocumentedInformation` entity (linked to Risk, Action, and Procedure) tracking whether records are *maintained* (living documents, §4.4.2(a)) versus *retained* (historical records, §4.4.2(b)) would make the EDQMS model audit-ready for §7.5 compliance.

---

## 9. Conclusion

The EDQMS ER-UML data model provides a structurally sound and standards-compliant foundation for an Event Driven Quality Management System. Its key architectural contributions are:

- The **Event entity** as a reactive and proactive trigger across all quality domains.
- The **Risk entity** with a `riskCategory` enumeration that honours ISO 9001:2015's dual concept of risk as both threat and opportunity.
- The **`riskPriorityNumber`** attribute that enables proportionate, evidence-based action selection (Cochran's RPN methodology).
- The **`actionApplication`** entity that classifies actions by their QMS process context, ensuring traceability from Risk to Action to ISO clause.
- A complete **ownership chain** (`User`, `Role`) wired into every entity, enforcing accountability at every level of the model.

The model implements the three interlocking principles that ISO 9001:2015 §0.3 identifies as fundamental to any effective quality management system: the **process approach**, the **PDCA cycle**, and **risk-based thinking**.

With the open items in Section 8 addressed — particularly the direct `Risk ↔ Action` relationship — the EDQMS will achieve full clause-level coverage from context (§4) through improvement (§10).

---

## References

- **ISO/FDIS 9001:2015(E).** *Quality management systems — Requirements.* International Organization for Standardization. → `ISO90012015_EN_ocr.pdf`
- **Cochran, C. (2015).** *ISO 9001:2015 in Plain English.* Paton Professional. ISBN 978-1-932828-72-6. → `iso-9001-2015-in-plain-english_Craig-Cochran_.md`
- **EDBPM Lucidchart diagram** (EDQMS-01 project): https://lucid.app/lucidchart/090097f0-5c82-40ac-999b-ff1c96ba5c94 — tab: EDQMS ER-UML.
