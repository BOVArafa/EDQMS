#!/usr/bin/env python3
"""
build_mockup_data.py — deterministic generator for mockup_data_prototype.json

Produces a curated, relationally-consistent demo dataset for the EDQMS "Global
Engineering Portal" prototype. Only *base* (user-entered) fields are stored;
computed/mirror/rollup fields are intentionally omitted and recomputed by
validate_mockup.py (that recomputation is the proof that every report in
datamodel.json is buildable).

Run:  python3 build_mockup_data.py   ->  writes mockup_data_prototype.json
"""
import json
import os

# ----------------------------------------------------------------------------
# Talent foundation
# ----------------------------------------------------------------------------
functions = [
    {"functionID": "F1", "functionName": "Electrical Design"},
    {"functionID": "F2", "functionName": "Mechanical Design"},
    {"functionID": "F3", "functionName": "Analysis"},
    {"functionID": "F4", "functionName": "Planning"},
    {"functionID": "F5", "functionName": "Quality"},
]

skill_levels = [
    {"skillLevelID": "SL1", "levelName": "Junior", "levelDescription": "0-3 years of experience", "levelRank": 1},
    {"skillLevelID": "SL2", "levelName": "Senior", "levelDescription": "4-8 years of experience", "levelRank": 2},
    {"skillLevelID": "SL3", "levelName": "Expert", "levelDescription": "9-15 years of experience", "levelRank": 3},
    {"skillLevelID": "SL4", "levelName": "Principal", "levelDescription": "15+ years of experience", "levelRank": 4},
]

graduation = [
    {"graduationID": "G1", "graduationName": "Electrical Engineering", "field": "Engineering"},
    {"graduationID": "G2", "graduationName": "Mechanical Engineering", "field": "Engineering"},
    {"graduationID": "G3", "graduationName": "Industrial Engineering", "field": "Engineering"},
    {"graduationID": "G4", "graduationName": "Technical Diploma", "field": "Technical"},
]

roles = [
    {"roleID": "R01", "roleName": "JR Electrical Designer", "functionID": "F1", "skillLevelID": "SL1", "graduationID": "G1", "quantity": 6, "isActive": True},
    {"roleID": "R02", "roleName": "SR Electrical Designer", "functionID": "F1", "skillLevelID": "SL2", "graduationID": "G1", "quantity": 4, "isActive": True},
    {"roleID": "R03", "roleName": "JR Mechanical Designer", "functionID": "F2", "skillLevelID": "SL1", "graduationID": "G2", "quantity": 5, "isActive": True},
    {"roleID": "R04", "roleName": "SR Mechanical Designer", "functionID": "F2", "skillLevelID": "SL2", "graduationID": "G2", "quantity": 4, "isActive": True},
    {"roleID": "R05", "roleName": "Expert Mechanical Designer", "functionID": "F2", "skillLevelID": "SL3", "graduationID": "G2", "quantity": 2, "isActive": True},
    {"roleID": "R06", "roleName": "Analyst", "functionID": "F3", "skillLevelID": "SL2", "graduationID": "G3", "quantity": 3, "isActive": True},
    {"roleID": "R07", "roleName": "SR Analyst", "functionID": "F3", "skillLevelID": "SL3", "graduationID": "G3", "quantity": 2, "isActive": True},
    {"roleID": "R08", "roleName": "Planner", "functionID": "F4", "skillLevelID": "SL2", "graduationID": "G3", "quantity": 3, "isActive": True},
    {"roleID": "R09", "roleName": "Quality Engineer", "functionID": "F5", "skillLevelID": "SL2", "graduationID": "G1", "quantity": 2, "isActive": True},
    {"roleID": "R10", "roleName": "Quality Manager", "functionID": "F5", "skillLevelID": "SL4", "graduationID": "G1", "quantity": 1, "isActive": True},
]
role_fn = {r["roleID"]: r["functionID"] for r in roles}

squads = [
    {"squadID": "SQ1", "squadName": "Core EMEA", "squadType": "internal", "managerName": "Klaus Berger", "managerEmail": "klaus.berger@siemens-energy.com"},
    {"squadID": "SQ2", "squadName": "Americas Ops", "squadType": "internal", "managerName": "Ana Souza", "managerEmail": "ana.souza@siemens-energy.com"},
    {"squadID": "SQ3", "squadName": "APAC Partners", "squadType": "outsource", "managerName": "Wei Chen", "managerEmail": "wei.chen@partner.com"},
]

# ----------------------------------------------------------------------------
# Customers / Factories
# ----------------------------------------------------------------------------
factories = [
    {"factoryID": "FC1", "factoryName": "PN", "city": "Nuremberg", "country": "Germany", "businessSegment": "LPT", "region": "EMEA", "isActive": True},
    {"factoryID": "FC2", "factoryName": "DR", "city": "Dresden", "country": "Germany", "businessSegment": "MT", "region": "EMEA", "isActive": True},
    {"factoryID": "FC3", "factoryName": "SP", "city": "Sao Paulo", "country": "Brazil", "businessSegment": "LPT", "region": "Americas", "isActive": True},
    {"factoryID": "FC4", "factoryName": "MX", "city": "Monterrey", "country": "Mexico", "businessSegment": "DT", "region": "Americas", "isActive": True},
    {"factoryID": "FC5", "factoryName": "SH", "city": "Shanghai", "country": "China", "businessSegment": "MT", "region": "APAC", "isActive": True},
    {"factoryID": "FC6", "factoryName": "MU", "city": "Mumbai", "country": "India", "businessSegment": "DT", "region": "APAC", "isActive": False},
]

# People: 24 people. Each has one role (roleID) whose function drives functionID.
_people_spec = [
    # userName, roleID, factoryID, squadID, personalCost, isActive
    ("Lena Fischer", "R02", "FC1", "SQ1", 95, True),
    ("Omar Haddad", "R01", "FC1", "SQ1", 62, True),
    ("Priya Nair", "R01", "FC1", "SQ1", 60, True),
    ("Tomas Novak", "R04", "FC1", "SQ1", 92, True),
    ("Sofia Rossi", "R04", "FC1", "SQ1", 90, True),
    ("Hugo Meyer", "R03", "FC1", "SQ1", 58, True),
    ("Marta Alves", "R03", "FC1", "SQ1", 57, True),
    ("Jan Kowalski", "R05", "FC2", "SQ1", 120, True),
    ("Eva Braun", "R06", "FC2", "SQ1", 78, True),
    ("Nils Andersson", "R07", "FC2", "SQ1", 105, True),
    ("Ingrid Holm", "R08", "FC1", "SQ1", 84, True),
    ("Pedro Gomes", "R08", "FC3", "SQ2", 80, True),
    ("Camila Dias", "R02", "FC3", "SQ2", 93, True),
    ("Rafael Lima", "R01", "FC3", "SQ2", 61, True),
    ("Bruna Costa", "R04", "FC3", "SQ2", 91, True),
    ("Diego Torres", "R03", "FC4", "SQ2", 56, True),
    ("Lucia Mendez", "R06", "FC4", "SQ2", 76, True),
    ("Mateus Rocha", "R01", "FC4", "SQ2", 59, True),
    ("Wei Zhang", "R04", "FC5", "SQ3", 70, True),
    ("Hana Kim", "R03", "FC5", "SQ3", 45, True),
    ("Arjun Patel", "R01", "FC5", "SQ3", 44, True),
    ("Mei Lin", "R06", "FC5", "SQ3", 55, True),
    ("Sara Vogel", "R09", "FC1", "SQ1", 88, True),
    ("Franz Keller", "R10", "FC1", "SQ1", 140, True),
]
people = []
for i, (name, roleID, fac, squad, cost, active) in enumerate(_people_spec, start=1):
    uid = "U%02d" % i
    email = name.lower().replace(" ", ".") + "@siemens-energy.com"
    people.append({
        "userID": uid, "userName": name, "userEmail": email,
        "location": fac, "isActive": active,
        "hireDate": "20%02d-03-15" % (15 + (i % 8)),
        "functionID": role_fn[roleID], "roleID": roleID,
        "personalCost": cost, "squadID": squad,
    })
# convenience: first person per role
person_by_role = {}
for p in people:
    person_by_role.setdefault(p["roleID"], p["userID"])

# ----------------------------------------------------------------------------
# Inventory
# ----------------------------------------------------------------------------
products = [
    {"productID": "P01", "productName": "GVT-800", "isActive": True},
    {"productID": "P02", "productName": "GVT-1200", "isActive": True},
    {"productID": "P03", "productName": "MPT-400", "isActive": True},
    {"productID": "P04", "productName": "MPT-630", "isActive": True},
    {"productID": "P05", "productName": "DPT-160", "isActive": True},
    {"productID": "P06", "productName": "DPT-250", "isActive": True},
    {"productID": "P07", "productName": "GVT-1600", "isActive": True},
    {"productID": "P08", "productName": "MPT-315", "isActive": True},
    {"productID": "P09", "productName": "DPT-100", "isActive": True},
    {"productID": "P10", "productName": "Bushing-Kit", "isActive": False},
]
product_class = [
    {"productClassID": "PC1", "voltageRate": "<=72.5kV", "powerRating": "<=100MVA"},
    {"productClassID": "PC2", "voltageRate": "<=145kV", "powerRating": "<=300MVA"},
    {"productClassID": "PC3", "voltageRate": "<=420kV", "powerRating": "<=800MVA"},
    {"productClassID": "PC4", "voltageRate": "<=36kV", "powerRating": "<=63MVA"},
    {"productClassID": "PC5", "voltageRate": "<=550kV", "powerRating": ">800MVA"},
]
product_groups = [
    {"productGroupID": "PG1", "businessSegment": "LPT", "products": "P01", "productClassID": ["PC3", "PC5"], "isActive": True},
    {"productGroupID": "PG2", "businessSegment": "LPT", "products": "P02", "productClassID": ["PC3"], "isActive": True},
    {"productGroupID": "PG3", "businessSegment": "MT", "products": "P03", "productClassID": ["PC2"], "isActive": True},
    {"productGroupID": "PG4", "businessSegment": "MT", "products": "P04", "productClassID": ["PC2"], "isActive": True},
    {"productGroupID": "PG5", "businessSegment": "DT", "products": "P05", "productClassID": ["PC4"], "isActive": True},
    {"productGroupID": "PG6", "businessSegment": "DT", "products": "P06", "productClassID": ["PC4"], "isActive": True},
]
scopes = [
    {"scopeID": "SC1", "scopeName": "Uprating", "scopeOpportunity": ["Increase Capability"], "isActive": True},
    {"scopeID": "SC2", "scopeName": "Temperature Reduction", "scopeOpportunity": ["lifetime Extension"], "isActive": True},
    {"scopeID": "SC3", "scopeName": "Redesign", "scopeOpportunity": ["Dieletic Failure", "lifetime Extension"], "isActive": True},
    {"scopeID": "SC4", "scopeName": "Life Extension", "scopeOpportunity": ["lifetime Extension"], "isActive": True},
    {"scopeID": "SC5", "scopeName": "Failure Analysis", "scopeOpportunity": ["Dieletic Failure"], "isActive": True},
]
product_scopes = [
    {"productScopeID": "PS01", "productGroupID": "PG1", "scopeID": "SC1", "isActive": True, "createdAt": "2026-01-10"},
    {"productScopeID": "PS02", "productGroupID": "PG1", "scopeID": "SC3", "isActive": True, "createdAt": "2026-01-12"},
    {"productScopeID": "PS03", "productGroupID": "PG2", "scopeID": "SC2", "isActive": True, "createdAt": "2026-01-15"},
    {"productScopeID": "PS04", "productGroupID": "PG3", "scopeID": "SC1", "isActive": True, "createdAt": "2026-02-01"},
    {"productScopeID": "PS05", "productGroupID": "PG3", "scopeID": "SC4", "isActive": True, "createdAt": "2026-02-05"},
    {"productScopeID": "PS06", "productGroupID": "PG4", "scopeID": "SC5", "isActive": True, "createdAt": "2026-02-10"},
    {"productScopeID": "PS07", "productGroupID": "PG5", "scopeID": "SC1", "isActive": True, "createdAt": "2026-03-01"},
    {"productScopeID": "PS08", "productGroupID": "PG5", "scopeID": "SC2", "isActive": True, "createdAt": "2026-03-04"},
    {"productScopeID": "PS09", "productGroupID": "PG6", "scopeID": "SC3", "isActive": True, "createdAt": "2026-03-08"},
    {"productScopeID": "PS10", "productGroupID": "PG2", "scopeID": "SC1", "isActive": True, "createdAt": "2026-03-12"},
]
# product/scope helpers per productScope
ps_product = {}
ps_scope = {}
for ps in product_scopes:
    grp = next(g for g in product_groups if g["productGroupID"] == ps["productGroupID"])
    ps_product[ps["productScopeID"]] = grp["products"]
    ps_scope[ps["productScopeID"]] = ps["scopeID"]

# ----------------------------------------------------------------------------
# Operation: Constraint Types, Constraints, Channels, Handouts
# ----------------------------------------------------------------------------
constraint_types = [
    {"constrainTypeID": "CT1", "constrainTypeName": "Operational"},
    {"constrainTypeID": "CT2", "constrainTypeName": "Design"},
    {"constrainTypeID": "CT3", "constrainTypeName": "Testing"},
    {"constrainTypeID": "CT4", "constrainTypeName": "Technical"},
    {"constrainTypeID": "CT5", "constrainTypeName": "Commercial"},
]
constraints = [
    {"constrainID": "CN1", "constrainName": "IEC 60076 Compliance", "constrainDescription": "General power transformer standard", "constrainTypeID": "CT4", "isActive": True, "regulatoryReference": "IEC 60076-1"},
    {"constrainID": "CN2", "constrainName": "Max Tank Weight", "constrainDescription": "Transport weight limit", "constrainTypeID": "CT2", "isActive": True, "regulatoryReference": None},
    {"constrainID": "CN3", "constrainName": "Short-circuit Withstand", "constrainDescription": "Mechanical withstand under fault", "constrainTypeID": "CT3", "isActive": True, "regulatoryReference": "IEC 60076-5"},
    {"constrainID": "CN4", "constrainName": "Delivery Lead Time", "constrainDescription": "Contractual delivery window", "constrainTypeID": "CT5", "isActive": True, "regulatoryReference": None},
    {"constrainID": "CN5", "constrainName": "Noise Level Limit", "constrainDescription": "Acoustic emission cap", "constrainTypeID": "CT1", "isActive": True, "regulatoryReference": "IEC 60076-10"},
    {"constrainID": "CN6", "constrainName": "Temperature Rise Limit", "constrainDescription": "Thermal rise limit", "constrainTypeID": "CT4", "isActive": True, "regulatoryReference": "IEC 60076-2"},
    {"constrainID": "CN7", "constrainName": "Insulation Level", "constrainDescription": "Dielectric design level", "constrainTypeID": "CT2", "isActive": True, "regulatoryReference": None},
    {"constrainID": "CN8", "constrainName": "Budget Cap", "constrainDescription": "Offer budget ceiling", "constrainTypeID": "CT5", "isActive": False, "regulatoryReference": None},
]
channels = [
    {"channelID": "CH1", "channelName": "Portal", "channelOwner": "Siemens Energy", "channelStatus": "Active"},
    {"channelID": "CH2", "channelName": "Salesforce", "channelOwner": "Salesforce Inc.", "channelStatus": "Active"},
    {"channelID": "CH3", "channelName": "Outlook", "channelOwner": "Microsoft", "channelStatus": "Active"},
    {"channelID": "CH4", "channelName": "Teams", "channelOwner": "Microsoft", "channelStatus": "Inactive"},
]
handouts = [
    {"handoutID": "HO01", "handoutName": "Requirement Spec", "handoutDescription": "Captured customer requirements", "createdAt": "2026-04-01", "channelID": "CH1", "type": "data", "templateTitle": "Req Spec Template"},
    {"handoutID": "HO02", "handoutName": "Electrical Datasheet", "handoutDescription": "Electrical sizing outputs", "createdAt": "2026-04-02", "channelID": "CH1", "type": "file", "templateTitle": "Datasheet Template"},
    {"handoutID": "HO03", "handoutName": "Offer Document", "handoutDescription": "Commercial offer package", "createdAt": "2026-04-03", "channelID": "CH2", "type": "file", "templateTitle": "Offer Template"},
    {"handoutID": "HO04", "handoutName": "Design Drawings", "handoutDescription": "Active part drawings", "createdAt": "2026-04-04", "channelID": "CH1", "type": "file", "templateTitle": "Drawing Template"},
    {"handoutID": "HO05", "handoutName": "Tank Layout", "handoutDescription": "Mechanical layout drawings", "createdAt": "2026-04-05", "channelID": "CH1", "type": "file", "templateTitle": "Layout Template"},
    {"handoutID": "HO06", "handoutName": "Review Report", "handoutDescription": "Peer review findings", "createdAt": "2026-04-06", "channelID": "CH3", "type": "file", "templateTitle": "Review Template"},
    {"handoutID": "HO07", "handoutName": "Compliance Certificate", "handoutDescription": "Standards compliance evidence", "createdAt": "2026-04-07", "channelID": "CH1", "type": "file", "templateTitle": "Cert Template"},
    {"handoutID": "HO08", "handoutName": "RCA Report", "handoutDescription": "Root cause analysis", "createdAt": "2026-04-08", "channelID": "CH3", "type": "file", "templateTitle": "RCA Template"},
    {"handoutID": "HO09", "handoutName": "Corrective Plan", "handoutDescription": "Corrective action plan", "createdAt": "2026-04-09", "channelID": "CH1", "type": "data", "templateTitle": "CAP Template"},
    {"handoutID": "HO10", "handoutName": "Thermal Report", "handoutDescription": "Thermal study results", "createdAt": "2026-04-10", "channelID": "CH1", "type": "file", "templateTitle": "Thermal Template"},
]

# ----------------------------------------------------------------------------
# Operation: Processes, Activities, Actions, Workflows
# ----------------------------------------------------------------------------
processes = [
    {"processID": "PR1", "processName": "Offer Calculation", "processSystemID": "SAP-0042", "processOwner": person_by_role["R08"], "processDescription": "Prepare technical-commercial offer", "parentProcessID": None, "processStatus": "Active", "processVersion": "v1.2"},
    {"processID": "PR2", "processName": "Detailed Design", "processSystemID": None, "processOwner": person_by_role["R02"], "processDescription": "Full engineering design package", "parentProcessID": None, "processStatus": "Active", "processVersion": "v2.0"},
    {"processID": "PR3", "processName": "Design Review", "processSystemID": None, "processOwner": person_by_role["R10"], "processDescription": "Quality gate review", "parentProcessID": "PR2", "processStatus": "Active", "processVersion": "v1.0"},
    {"processID": "PR4", "processName": "Failure Investigation", "processSystemID": "SAP-0099", "processOwner": person_by_role["R09"], "processDescription": "Field failure root cause", "parentProcessID": None, "processStatus": "Active", "processVersion": "v1.1"},
    {"processID": "PR5", "processName": "Uprating Study", "processSystemID": None, "processOwner": person_by_role["R07"], "processDescription": "Assess uprating feasibility", "parentProcessID": None, "processStatus": "Active", "processVersion": "v1.3"},
]

# activities: (activityID, name, processID, default roleID, default execTime)
activities = [
    # PR1 — four activities so the Capacity test scenario (4 tasks) maps 1:1
    {"activityID": "A01", "activityName": "Requirement Capture", "processID": "PR1", "roleID": "R01", "execTime": 5, "procedureID": "PRC-101"},
    {"activityID": "A02", "activityName": "Electrical Sizing", "processID": "PR1", "roleID": "R04", "execTime": 8, "procedureID": "PRC-102"},
    {"activityID": "A03", "activityName": "Offer Costing", "processID": "PR1", "roleID": "R03", "execTime": 8, "procedureID": "PRC-103"},
    {"activityID": "A04", "activityName": "Mechanical Sizing", "processID": "PR1", "roleID": "R04", "execTime": 15, "procedureID": "PRC-104"},
    # PR2
    {"activityID": "A05", "activityName": "Electrical Design", "processID": "PR2", "roleID": "R02", "execTime": 20, "procedureID": "PRC-201"},
    {"activityID": "A06", "activityName": "Mechanical Layout", "processID": "PR2", "roleID": "R04", "execTime": 18, "procedureID": "PRC-202"},
    {"activityID": "A07", "activityName": "Design Documentation", "processID": "PR2", "roleID": "R03", "execTime": 12, "procedureID": "PRC-203"},
    # PR3
    {"activityID": "A08", "activityName": "Peer Review", "processID": "PR3", "roleID": "R05", "execTime": 6, "procedureID": "PRC-301"},
    {"activityID": "A09", "activityName": "Compliance Check", "processID": "PR3", "roleID": "R09", "execTime": 4, "procedureID": "PRC-302"},
    # PR4
    {"activityID": "A10", "activityName": "Root Cause Analysis", "processID": "PR4", "roleID": "R07", "execTime": 16, "procedureID": "PRC-401"},
    {"activityID": "A11", "activityName": "Corrective Proposal", "processID": "PR4", "roleID": "R06", "execTime": 10, "procedureID": "PRC-402"},
    # PR5
    {"activityID": "A12", "activityName": "Load Assessment", "processID": "PR5", "roleID": "R06", "execTime": 9, "procedureID": "PRC-501"},
    {"activityID": "A13", "activityName": "Thermal Study", "processID": "PR5", "roleID": "R07", "execTime": 14, "procedureID": "PRC-502"},
    {"activityID": "A14", "activityName": "Uprating Report", "processID": "PR5", "roleID": "R06", "execTime": 7, "procedureID": "PRC-503"},
]
act_by_id = {a["activityID"]: a for a in activities}

# actions: one per activity
_action_names = {
    "A01": "Capture Requirements", "A02": "Size Windings", "A03": "Cost Offer", "A04": "Size Core & Tank",
    "A05": "Design Active Part", "A06": "Layout Tank", "A07": "Produce Drawings", "A08": "Review Design",
    "A09": "Check Compliance", "A10": "Analyze Root Cause", "A11": "Propose Correction",
    "A12": "Assess Load", "A13": "Study Thermal", "A14": "Write Uprating Report",
}
# risk/application linkage for a subset (rest null)
_action_links = {
    "A08": ("RK03", "AP2"),   # Review Design -> Control
    "A09": ("RK01", "AP2"),   # Compliance -> Control
    "A10": ("RK05", "AP5"),   # Root cause -> Improvement
    "A11": ("RK05", "AP1"),   # Corrective proposal -> Risk Management
    "A02": ("RK02", "AP1"),   # Sizing -> Risk Management
    "A13": ("RK06", "AP4"),   # Thermal -> Monitoring
}
actions = []
for i, a in enumerate(activities, start=1):
    aid = "AC%02d" % i
    risk, appl = _action_links.get(a["activityID"], (None, None))
    actions.append({
        "actionID": aid, "actionName": _action_names[a["activityID"]],
        "actionDescription": "Procedure to %s" % _action_names[a["activityID"]].lower(),
        "activityID": a["activityID"], "riskID": risk, "applicationID": appl,
    })
action_by_activity = {a["activityID"]: ac["actionID"] for a, ac in zip(activities, actions)}

# workflows: one step per activity, ordered within a process by activity order
workflows = []
_prev_by_process = {}
for i, a in enumerate(activities, start=1):
    wid = "WF%02d" % i
    parent = _prev_by_process.get(a["processID"])
    workflows.append({
        "workflowID": wid, "processID": a["processID"],
        "activities": a["activityID"], "parentStepID": parent,
    })
    _prev_by_process[a["processID"]] = wid
workflow_by_activity = {a["activityID"]: w["workflowID"] for a, w in zip(activities, workflows)}

# ----------------------------------------------------------------------------
# Operation: Sources / Source Categories / Requirements (Quality module lookups
# referenced by Events, so defined before Events)
# ----------------------------------------------------------------------------
source_categories = [
    {"sourceCategoryID": "SCAT1", "sourceCategoryName": "Customer", "sourceCategoryDescription": "Customer-originated issues and requests"},
    {"sourceCategoryID": "SCAT2", "sourceCategoryName": "Regulatory", "sourceCategoryDescription": "Standards and statutory bodies"},
    {"sourceCategoryID": "SCAT3", "sourceCategoryName": "Internal", "sourceCategoryDescription": "Internal audits and lessons learned"},
    {"sourceCategoryID": "SCAT4", "sourceCategoryName": "Supplier", "sourceCategoryDescription": "Externally provided processes"},
]
sources = [
    {"sourceID": "SRC1", "sourceName": "Key Account - Grid Co", "sourceCategoryID": "SCAT1", "sourceOwner": person_by_role["R08"], "sourceDescription": "Major utility customer", "isActive": True},
    {"sourceID": "SRC2", "sourceName": "IEC Technical Committee", "sourceCategoryID": "SCAT2", "sourceOwner": person_by_role["R10"], "sourceDescription": "Standards updates", "isActive": True},
    {"sourceID": "SRC3", "sourceName": "Internal Quality Audit", "sourceCategoryID": "SCAT3", "sourceOwner": person_by_role["R09"], "sourceDescription": "Annual QMS audit", "isActive": True},
    {"sourceID": "SRC4", "sourceName": "Field Service Reports", "sourceCategoryID": "SCAT1", "sourceOwner": person_by_role["R07"], "sourceDescription": "Warranty and field failures", "isActive": True},
    {"sourceID": "SRC5", "sourceName": "Bushing Supplier", "sourceCategoryID": "SCAT4", "sourceOwner": person_by_role["R09"], "sourceDescription": "Component supplier", "isActive": True},
    {"sourceID": "SRC6", "sourceName": "Legacy Program Review", "sourceCategoryID": "SCAT3", "sourceOwner": person_by_role["R10"], "sourceDescription": "Deprecated program", "isActive": False},
]
requirements = [
    {"requirementID": "RQ1", "requirementName": "Uprating without capacity loss", "requirementDescription": "Increase rating keeping footprint", "sourceID": "SRC1", "requirementType": "Customer", "isActive": True, "productID": "P01"},
    {"requirementID": "RQ2", "requirementName": "IEC 60076-5 short-circuit", "requirementDescription": "Meet latest withstand", "sourceID": "SRC2", "requirementType": "Regulatory", "isActive": True, "productID": "P03"},
    {"requirementID": "RQ3", "requirementName": "Noise below 65 dB", "requirementDescription": "Acoustic limit urban site", "sourceID": "SRC1", "requirementType": "Customer", "isActive": True, "productID": "P02"},
    {"requirementID": "RQ4", "requirementName": "Traceable design records", "requirementDescription": "Audit-ready documentation", "sourceID": "SRC3", "requirementType": "Internal", "isActive": True, "productID": None},
    {"requirementID": "RQ5", "requirementName": "Bushing dielectric conformity", "requirementDescription": "Supplier part conformity", "sourceID": "SRC5", "requirementType": "Statutory", "isActive": True, "productID": "P10"},
    {"requirementID": "RQ6", "requirementName": "Thermal rise <= 65K", "requirementDescription": "Temperature rise limit", "sourceID": "SRC2", "requirementType": "Regulatory", "isActive": True, "productID": "P04"},
    {"requirementID": "RQ7", "requirementName": "On-time delivery 95%", "requirementDescription": "Contractual OTD", "sourceID": "SRC1", "requirementType": "Customer", "isActive": True, "productID": None},
    {"requirementID": "RQ8", "requirementName": "Failure recurrence < 2%", "requirementDescription": "Corrective effectiveness", "sourceID": "SRC4", "requirementType": "Internal", "isActive": False, "productID": "P05"},
]

# ----------------------------------------------------------------------------
# Operation: Events (each triggers exactly one process via its tasks; sourceID set)
# ----------------------------------------------------------------------------
events = [
    {"eventID": "E1", "eventTitle": "Offer Calculation Requested", "eventDescription": "Customer requests a technical-commercial offer", "eventCreatedAt": "2026-05-02T09:00:00", "sourceID": "SRC1", "_process": "PR1"},
    {"eventID": "E2", "eventTitle": "Design Package Requested", "eventDescription": "Awarded project needs full design", "eventCreatedAt": "2026-05-06T10:30:00", "sourceID": "SRC1", "_process": "PR2"},
    {"eventID": "E3", "eventTitle": "Design Review Triggered", "eventDescription": "Design reaches review gate", "eventCreatedAt": "2026-05-09T14:00:00", "sourceID": "SRC3", "_process": "PR3"},
    {"eventID": "E4", "eventTitle": "Field Failure Reported", "eventDescription": "Unit failure reported from field", "eventCreatedAt": "2026-05-14T08:15:00", "sourceID": "SRC4", "_process": "PR4"},
    {"eventID": "E5", "eventTitle": "Uprating Study Requested", "eventDescription": "Customer explores uprating", "eventCreatedAt": "2026-05-20T11:45:00", "sourceID": "SRC1", "_process": "PR5"},
    {"eventID": "E6", "eventTitle": "Customer Change Request", "eventDescription": "Scope change on active design", "eventCreatedAt": "2026-05-25T16:20:00", "sourceID": "SRC2", "_process": "PR2"},
]
event_process = {e["eventID"]: e["_process"] for e in events}
for e in events:
    del e["_process"]

# ----------------------------------------------------------------------------
# Operation: Tasks
#   Base fields per task: taskID, eventID, processID, activityID, actionID,
#   productScopeID, executionTime, roleID, constrainIDs, taskInputID,
#   taskOutputID, customerName(factoryID), parentStepID(workflowID)
#   Generated as: for each (event, productScope) forecast/ticket combination,
#   instantiate the triggered process's activities as tasks.
# ----------------------------------------------------------------------------
# handout per activity (input/output)
_io = {
    "A01": ("HO01", "HO01"), "A02": ("HO01", "HO02"), "A03": ("HO02", "HO03"), "A04": ("HO01", "HO05"),
    "A05": ("HO02", "HO04"), "A06": ("HO04", "HO05"), "A07": ("HO05", "HO04"), "A08": ("HO04", "HO06"),
    "A09": ("HO06", "HO07"), "A10": ("HO01", "HO08"), "A11": ("HO08", "HO09"),
    "A12": ("HO01", "HO10"), "A13": ("HO10", "HO10"), "A14": ("HO10", "HO03"),
}
_constraints_for_activity = {
    "A02": ["CN1", "CN7"], "A04": ["CN2"], "A05": ["CN1", "CN7"], "A06": ["CN2", "CN5"],
    "A08": ["CN1"], "A09": ["CN1", "CN3"], "A13": ["CN6"], "A12": ["CN6"],
}

tasks = []
# (event, productScope, factory) combinations that will drive forecast scopes and tickets
# defined explicitly so forecast scopes / tickets can reference the same tasks.
task_combos = [
    # comboKey, eventID, productScopeID, factoryID
    ("C1", "E1", "PS01", "FC1"),   # scenario combo (Offer Calc, LPT Uprating, PN)
    ("C2", "E2", "PS01", "FC1"),
    ("C3", "E5", "PS02", "FC1"),
    ("C4", "E1", "PS04", "FC3"),
    ("C5", "E2", "PS04", "FC3"),
    ("C6", "E3", "PS04", "FC3"),
    ("C7", "E4", "PS06", "FC5"),
    ("C8", "E1", "PS07", "FC4"),
    ("C9", "E5", "PS05", "FC5"),
    ("C10", "E2", "PS03", "FC2"),
    ("C11", "E1", "PS08", "FC4"),
    ("C12", "E4", "PS09", "FC5"),
]
combo_tasks = {}   # comboKey -> list of taskIDs
_next_task = 1


def _mk_task(taskID, event, ps, factory, activity, roleID=None, execTime=None):
    a = act_by_id[activity]
    tin, tout = _io[activity]
    tasks.append({
        "taskID": taskID,
        "eventID": event,
        "processID": a["processID"],
        "activityID": activity,
        "actionID": action_by_activity[activity],
        "productScopeID": ps,
        "executionTime": execTime if execTime is not None else a["execTime"],
        "roleID": roleID if roleID is not None else a["roleID"],
        "constrainIDs": _constraints_for_activity.get(activity, []),
        "taskInputID": tin,
        "taskOutputID": tout,
        "customerName": factory,
        "parentStepID": workflow_by_activity[activity],
    })


# --- Scenario combo C1: exact taskIDs/roles/times from dashboard-reports-analysis.md
# Offer Calculation (PR1) activities A01..A04 -> tasks 012, 032, 033, 045
_scenario = [
    ("012", "A01", "R01", 5),
    ("032", "A02", "R04", 8),
    ("033", "A03", "R03", 8),
    ("045", "A04", "R04", 15),
]
for tid, act, role, et in _scenario:
    _mk_task(tid, "E1", "PS01", "FC1", act, role, et)
combo_tasks["C1"] = [t[0] for t in _scenario]

# --- Remaining combos: instantiate the triggered process activities
for combo in task_combos:
    key, ev, ps, fac = combo
    if key == "C1":
        continue
    proc = event_process[ev]
    ids = []
    for a in activities:
        if a["processID"] != proc:
            continue
        tid = "%03d" % (100 + _next_task)
        _next_task += 1
        _mk_task(tid, ev, ps, fac, a["activityID"])
        ids.append(tid)
    combo_tasks[key] = ids

# ----------------------------------------------------------------------------
# Customers: Forecasts & Forecast Scopes
# ----------------------------------------------------------------------------
forecasts = [
    {"forecastID": "FO1", "factoryID": "FC1", "forecastPeriod": "Annual", "forecastYear": 2026, "forecastQuarter": None, "forecastMonth": None, "periodStart": "2026-01", "periodFinish": "2026-12", "status": "Approved", "createdBy": person_by_role["R08"], "createdAt": "2025-12-01T09:00:00"},
    # FO2 == Capacity Report-A test forecast (periodStart 09-2026, periodFinish 01-2027)
    {"forecastID": "FO2", "factoryID": "FC1", "forecastPeriod": "Quarter", "forecastYear": 2026, "forecastQuarter": 4, "forecastMonth": None, "periodStart": "2026-09", "periodFinish": "2027-01", "status": "Submitted", "createdBy": person_by_role["R08"], "createdAt": "2026-08-15T10:00:00"},
    {"forecastID": "FO3", "factoryID": "FC3", "forecastPeriod": "Quarter", "forecastYear": 2026, "forecastQuarter": 3, "forecastMonth": None, "periodStart": "2026-07", "periodFinish": "2026-11", "status": "Approved", "createdBy": person_by_role["R08"], "createdAt": "2026-06-10T09:30:00"},
    {"forecastID": "FO4", "factoryID": "FC5", "forecastPeriod": "Month", "forecastYear": 2026, "forecastQuarter": None, "forecastMonth": 10, "periodStart": "2026-10", "periodFinish": "2026-10", "status": "Draft", "createdBy": person_by_role["R08"], "createdAt": "2026-09-20T08:00:00"},
    {"forecastID": "FO5", "factoryID": "FC4", "forecastPeriod": "Annual", "forecastYear": 2027, "forecastQuarter": None, "forecastMonth": None, "periodStart": "2027-01", "periodFinish": "2027-12", "status": "Draft", "createdBy": person_by_role["R08"], "createdAt": "2026-11-05T09:00:00"},
    {"forecastID": "FO6", "factoryID": "FC2", "forecastPeriod": "Quarter", "forecastYear": 2026, "forecastQuarter": 4, "forecastMonth": None, "periodStart": "2026-10", "periodFinish": "2027-02", "status": "Submitted", "createdBy": person_by_role["R08"], "createdAt": "2026-09-25T11:00:00"},
]
# forecast scopes reference the combos (event + productScope) so tasks roll up
forecast_scopes = [
    {"forecastScopeID": "FS01", "forecastID": "FO2", "productScopeID": "PS01", "eventID": "E1", "notes": "Offer calc capacity (scenario)"},
    {"forecastScopeID": "FS02", "forecastID": "FO2", "productScopeID": "PS01", "eventID": "E2", "notes": "Design package demand"},
    {"forecastScopeID": "FS03", "forecastID": "FO2", "productScopeID": "PS02", "eventID": "E5", "notes": "Uprating study"},
    {"forecastScopeID": "FS04", "forecastID": "FO1", "productScopeID": "PS01", "eventID": "E1", "notes": ""},
    {"forecastScopeID": "FS05", "forecastID": "FO1", "productScopeID": "PS02", "eventID": "E5", "notes": ""},
    {"forecastScopeID": "FS06", "forecastID": "FO3", "productScopeID": "PS04", "eventID": "E1", "notes": ""},
    {"forecastScopeID": "FS07", "forecastID": "FO3", "productScopeID": "PS04", "eventID": "E2", "notes": ""},
    {"forecastScopeID": "FS08", "forecastID": "FO3", "productScopeID": "PS04", "eventID": "E3", "notes": ""},
    {"forecastScopeID": "FS09", "forecastID": "FO4", "productScopeID": "PS06", "eventID": "E4", "notes": ""},
    {"forecastScopeID": "FS10", "forecastID": "FO4", "productScopeID": "PS05", "eventID": "E5", "notes": ""},
    {"forecastScopeID": "FS11", "forecastID": "FO5", "productScopeID": "PS07", "eventID": "E1", "notes": ""},
    {"forecastScopeID": "FS12", "forecastID": "FO5", "productScopeID": "PS08", "eventID": "E1", "notes": ""},
    {"forecastScopeID": "FS13", "forecastID": "FO6", "productScopeID": "PS03", "eventID": "E2", "notes": ""},
    {"forecastScopeID": "FS14", "forecastID": "FO6", "productScopeID": "PS09", "eventID": "E4", "notes": ""},
    {"forecastScopeID": "FS15", "forecastID": "FO2", "productScopeID": "PS04", "eventID": "E1", "notes": ""},
    {"forecastScopeID": "FS16", "forecastID": "FO3", "productScopeID": "PS06", "eventID": "E4", "notes": ""},
    {"forecastScopeID": "FS17", "forecastID": "FO1", "productScopeID": "PS03", "eventID": "E2", "notes": ""},
    {"forecastScopeID": "FS18", "forecastID": "FO5", "productScopeID": "PS08", "eventID": "E2", "notes": ""},
]

# ----------------------------------------------------------------------------
# Workload: Projects, Tickets, Jobs
# ----------------------------------------------------------------------------
projects = [
    {"projectID": "0031", "projectName": "Grid Co Uprating", "clientName": "National Grid Co", "customerName": "FC1", "projectOwner": person_by_role["R08"], "projectStatus": "In Progress"},
    {"projectID": "0032", "projectName": "Metro Substation", "clientName": "Metro Utility", "customerName": "FC1", "projectOwner": person_by_role["R02"], "projectStatus": "In Progress"},
    {"projectID": "0033", "projectName": "SP Rewind", "clientName": "Brasil Energia", "customerName": "FC3", "projectOwner": person_by_role["R08"], "projectStatus": "Planning"},
    {"projectID": "0034", "projectName": "MX Distribution", "clientName": "CFE", "customerName": "FC4", "projectOwner": person_by_role["R08"], "projectStatus": "In Progress"},
    {"projectID": "0035", "projectName": "SH Failure Fix", "clientName": "State Grid", "customerName": "FC5", "projectOwner": person_by_role["R09"], "projectStatus": "On Hold"},
    {"projectID": "0036", "projectName": "DR Cooling Upgrade", "clientName": "EnBW", "customerName": "FC2", "projectOwner": person_by_role["R07"], "projectStatus": "In Progress"},
    {"projectID": "0037", "projectName": "APAC Uprating Study", "clientName": "State Grid", "customerName": "FC5", "projectOwner": person_by_role["R07"], "projectStatus": "Closed"},
    {"projectID": "0038", "projectName": "Legacy Support", "clientName": "National Grid Co", "customerName": "FC1", "projectOwner": person_by_role["R08"], "projectStatus": "Closed"},
]

# Tickets — one per relevant combo, linked to a forecast scope + project.
# ticket 001 == scenario (customer FC1, event E1, resolutionTime 2026-10-25).
tickets = [
    {"ticketID": "001", "projectID": "0031", "customerName": "FC1", "eventID": "E1", "forecastScopeID": "FS01", "ticketOwner": person_by_role["R08"], "ticketStatus": "InProgress", "targetDate": "2026-10-25", "ticketCreatedAt": "2026-09-28T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-10-25", "isEscalated": False, "escalatedToEventID": None, "_combo": "C1"},
    {"ticketID": "002", "projectID": "0031", "customerName": "FC1", "eventID": "E2", "forecastScopeID": "FS02", "ticketOwner": person_by_role["R02"], "ticketStatus": "Open", "targetDate": "2026-11-30", "ticketCreatedAt": "2026-10-05T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-11-28", "isEscalated": False, "escalatedToEventID": None, "_combo": "C2"},
    {"ticketID": "003", "projectID": "0032", "customerName": "FC1", "eventID": "E5", "forecastScopeID": "FS03", "ticketOwner": person_by_role["R07"], "ticketStatus": "Resolved", "targetDate": "2026-09-30", "ticketCreatedAt": "2026-08-20T09:00:00", "ticketClosedAt": "2026-09-27T15:00:00", "resolutionTime": "2026-09-27", "isEscalated": False, "escalatedToEventID": None, "_combo": "C3"},
    {"ticketID": "004", "projectID": "0033", "customerName": "FC3", "eventID": "E1", "forecastScopeID": "FS06", "ticketOwner": person_by_role["R08"], "ticketStatus": "Closed", "targetDate": "2026-08-15", "ticketCreatedAt": "2026-07-10T09:00:00", "ticketClosedAt": "2026-08-14T12:00:00", "resolutionTime": "2026-08-14", "isEscalated": False, "escalatedToEventID": None, "_combo": "C4"},
    {"ticketID": "005", "projectID": "0033", "customerName": "FC3", "eventID": "E2", "forecastScopeID": "FS07", "ticketOwner": person_by_role["R02"], "ticketStatus": "InProgress", "targetDate": "2026-10-31", "ticketCreatedAt": "2026-09-15T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-10-30", "isEscalated": False, "escalatedToEventID": None, "_combo": "C5"},
    {"ticketID": "006", "projectID": "0033", "customerName": "FC3", "eventID": "E3", "forecastScopeID": "FS08", "ticketOwner": person_by_role["R10"], "ticketStatus": "Open", "targetDate": "2026-11-15", "ticketCreatedAt": "2026-10-12T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-11-14", "isEscalated": False, "escalatedToEventID": None, "_combo": "C6"},
    {"ticketID": "007", "projectID": "0035", "customerName": "FC5", "eventID": "E4", "forecastScopeID": "FS09", "ticketOwner": person_by_role["R09"], "ticketStatus": "Escalated", "targetDate": "2026-10-20", "ticketCreatedAt": "2026-09-30T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-10-18", "isEscalated": True, "escalatedToEventID": "E4", "_combo": "C7"},
    {"ticketID": "008", "projectID": "0034", "customerName": "FC4", "eventID": "E1", "forecastScopeID": "FS11", "ticketOwner": person_by_role["R08"], "ticketStatus": "InProgress", "targetDate": "2026-11-10", "ticketCreatedAt": "2026-10-01T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-11-08", "isEscalated": False, "escalatedToEventID": None, "_combo": "C8"},
    {"ticketID": "009", "projectID": "0037", "customerName": "FC5", "eventID": "E5", "forecastScopeID": "FS10", "ticketOwner": person_by_role["R07"], "ticketStatus": "Closed", "targetDate": "2026-09-15", "ticketCreatedAt": "2026-08-01T09:00:00", "ticketClosedAt": "2026-09-12T14:00:00", "resolutionTime": "2026-09-12", "isEscalated": False, "escalatedToEventID": None, "_combo": "C9"},
    {"ticketID": "010", "projectID": "0036", "customerName": "FC2", "eventID": "E2", "forecastScopeID": "FS13", "ticketOwner": person_by_role["R02"], "ticketStatus": "InProgress", "targetDate": "2026-12-05", "ticketCreatedAt": "2026-10-20T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-12-03", "isEscalated": False, "escalatedToEventID": None, "_combo": "C10"},
    {"ticketID": "011", "projectID": "0034", "customerName": "FC4", "eventID": "E1", "forecastScopeID": "FS12", "ticketOwner": person_by_role["R08"], "ticketStatus": "Open", "targetDate": "2026-11-20", "ticketCreatedAt": "2026-10-22T09:00:00", "ticketClosedAt": None, "resolutionTime": "2026-11-18", "isEscalated": False, "escalatedToEventID": None, "_combo": "C11"},
    {"ticketID": "012", "projectID": "0035", "customerName": "FC5", "eventID": "E4", "forecastScopeID": "FS14", "ticketOwner": person_by_role["R09"], "ticketStatus": "Resolved", "targetDate": "2026-10-10", "ticketCreatedAt": "2026-09-05T09:00:00", "ticketClosedAt": "2026-10-08T16:00:00", "resolutionTime": "2026-10-08", "isEscalated": False, "escalatedToEventID": None, "_combo": "C12"},
]
combo_by_ticket = {t["ticketID"]: t["_combo"] for t in tickets}
for t in tickets:
    del t["_combo"]

# Jobs — created from a ticket's tasks; assignee's role matches the task role.
# realExecutionTime tracked via real dates. Spread across weeks Sep-Nov 2026.
jobs = []
_job_seq = 1
# a spread of weekly start dates (Mondays) to drive the throughput line chart
_weeks = ["2026-09-07", "2026-09-14", "2026-09-21", "2026-09-28",
          "2026-10-05", "2026-10-12", "2026-10-19", "2026-10-26",
          "2026-11-02", "2026-11-09"]
# person pool per role for assignment variety
role_people = {}
for p in people:
    role_people.setdefault(p["roleID"], []).append(p["userID"])


def _add_days(dstr, days):
    # lightweight date add without importing datetime for the whole file
    import datetime as _dt
    d = _dt.date.fromisoformat(dstr)
    return (d + _dt.timedelta(days=days)).isoformat()


_job_status_cycle = ["Done", "Done", "Active", "Done", "Queued", "Done", "Active", "Stoped", "Done", "Active"]
for ti, t in enumerate(tickets):
    combo = combo_by_ticket[t["ticketID"]]
    tlist = combo_tasks[combo]
    for tj, taskID in enumerate(tlist):
        task = next(tk for tk in tasks if tk["taskID"] == taskID)
        roleID = task["roleID"]
        assignees = role_people.get(roleID) or [person_by_role.get(roleID)]
        userID = assignees[(ti + tj) % len(assignees)]
        planned = task["executionTime"]
        week = _weeks[(ti + tj) % len(_weeks)]
        start = week
        end = _add_days(start, max(1, round(planned / 8)))
        status = _job_status_cycle[(ti + tj) % len(_job_status_cycle)]
        # actual dates + real execution: introduce variance (some overruns/underruns)
        variance_hours = [0, 3, -2, 6, 1, -1, 8, 2, -3, 4][(ti + tj) % 10]
        real_exec = max(1, planned + variance_hours)
        if status in ("Done", "Active", "Stoped"):
            real_start = _add_days(start, 1)
            real_end = _add_days(real_start, max(1, round(real_exec / 8)))
        else:
            real_start = None
            real_end = None
        jid = "J%03d" % _job_seq
        _job_seq += 1
        pred = ("J%03d" % (_job_seq - 2)) if tj > 0 else None
        jobs.append({
            "jobID": jid,
            "jobName": act_by_id[task["activityID"]]["activityName"],
            "ticketID": t["ticketID"],
            "taskID": taskID,
            "userID": userID,
            "projectName": next(pr["projectName"] for pr in projects if pr["projectID"] == t["projectID"]),
            "startDate": start,
            "endDate": end,
            "realStartDate": real_start,
            "realEndDate": real_end,
            "realExecutionTime": (real_exec if real_end else None),
            "predecesorJob": pred,
            "dependencyType": ("Finish-to-Start" if pred else None),
            "jobStatus": status,
        })

# ----------------------------------------------------------------------------
# Talent: Competence & Onboarding
# ----------------------------------------------------------------------------
# Competence: map a role to the scope/product it is certified for (via tasks it performs)
competence = []
_comp_seq = 1
_comp_specs = [
    # roleID, scopeID, productID, skillLevelID, isRequired
    ("R01", "SC1", "P01", "SL1", True),
    ("R02", "SC1", "P01", "SL2", True),
    ("R03", "SC1", "P01", "SL1", True),
    ("R04", "SC1", "P01", "SL2", True),
    ("R04", "SC3", "P01", "SL2", True),
    ("R05", "SC3", "P01", "SL3", True),
    ("R06", "SC5", "P04", "SL2", True),
    ("R07", "SC4", "P03", "SL3", True),
    ("R07", "SC5", "P05", "SL3", True),
    ("R09", "SC1", "P03", "SL2", True),
    ("R02", "SC2", "P02", "SL2", False),
    ("R04", "SC1", "P05", "SL2", True),
]
for roleID, scopeID, productID, sl, req in _comp_specs:
    competence.append({
        "competenceID": "CMP%02d" % _comp_seq,
        "roleID": roleID, "scopeID": scopeID, "productID": productID,
        "skillLevelID": sl, "isRequired": req,
    })
    _comp_seq += 1

# Onboarding: per person, certification status against their role's competences
onboarding = []
_onb_seq = 1
for p in people:
    comps = [c for c in competence if c["roleID"] == p["roleID"]]
    for c in comps:
        # certify most; leave a few uncertified to make the heatmap non-uniform
        certified = not (p["userID"] in ("U03", "U18", "U21") and c["isRequired"])
        onboarding.append({
            "onboardID": "ONB%03d" % _onb_seq,
            "userID": p["userID"],
            "competenceID": c["competenceID"],
            "isCertified": certified,
            "certifications": ("CERT-%s-%s" % (p["userID"], c["competenceID"]) if certified else ""),
        })
        _onb_seq += 1

# ----------------------------------------------------------------------------
# Quality: Risks, actionApplication, Event Log
# ----------------------------------------------------------------------------
action_application = [
    {"applicationID": "AP1", "applicationName": "Risk Management", "applicationDescription": "Actions to address risks and opportunities", "isoClause": "6.1.2"},
    {"applicationID": "AP2", "applicationName": "Control", "applicationDescription": "Operational control actions", "isoClause": "8"},
    {"applicationID": "AP3", "applicationName": "Communication", "applicationDescription": "Communication actions", "isoClause": "7.4"},
    {"applicationID": "AP4", "applicationName": "Monitoring", "applicationDescription": "Monitoring and measurement actions", "isoClause": "9.1"},
    {"applicationID": "AP5", "applicationName": "Improvement", "applicationDescription": "Improvement actions", "isoClause": "10"},
]
risks = [
    {"riskID": "RK01", "riskTitle": "Non-compliance with IEC 60076-5", "riskDescription": "Design may not meet latest short-circuit withstand", "riskCategory": "Threat", "riskSeverity": 5, "riskLikelihood": 3, "riskOwner": person_by_role["R10"], "riskStatus": "UnderTreatment", "riskCreatedAt": "2026-05-10T09:00:00", "riskReviewedAt": "2026-09-01T09:00:00", "eventID": "E3", "requirementID": "RQ2"},
    {"riskID": "RK02", "riskTitle": "Undersized windings", "riskDescription": "Electrical sizing error under load", "riskCategory": "Threat", "riskSeverity": 4, "riskLikelihood": 2, "riskOwner": person_by_role["R02"], "riskStatus": "Open", "riskCreatedAt": "2026-05-12T09:00:00", "riskReviewedAt": None, "eventID": "E1", "requirementID": "RQ1"},
    {"riskID": "RK03", "riskTitle": "Design review bottleneck", "riskDescription": "Single expert reviewer causes delay", "riskCategory": "Threat", "riskSeverity": 3, "riskLikelihood": 4, "riskOwner": person_by_role["R10"], "riskStatus": "UnderTreatment", "riskCreatedAt": "2026-05-15T09:00:00", "riskReviewedAt": "2026-08-20T09:00:00", "eventID": "E3", "requirementID": "RQ4"},
    {"riskID": "RK04", "riskTitle": "Uprating growth opportunity", "riskDescription": "Fleet uprating demand rising", "riskCategory": "Opportunity", "riskSeverity": 2, "riskLikelihood": 4, "riskOwner": person_by_role["R08"], "riskStatus": "Open", "riskCreatedAt": "2026-05-18T09:00:00", "riskReviewedAt": None, "eventID": "E5", "requirementID": "RQ1"},
    {"riskID": "RK05", "riskTitle": "Field failure recurrence", "riskDescription": "Repeat dielectric failures", "riskCategory": "Threat", "riskSeverity": 5, "riskLikelihood": 4, "riskOwner": person_by_role["R09"], "riskStatus": "UnderTreatment", "riskCreatedAt": "2026-05-20T09:00:00", "riskReviewedAt": "2026-09-10T09:00:00", "eventID": "E4", "requirementID": "RQ8"},
    {"riskID": "RK06", "riskTitle": "Thermal margin exceedance", "riskDescription": "Temperature rise near limit", "riskCategory": "Threat", "riskSeverity": 3, "riskLikelihood": 3, "riskOwner": person_by_role["R07"], "riskStatus": "Open", "riskCreatedAt": "2026-05-22T09:00:00", "riskReviewedAt": None, "eventID": "E5", "requirementID": "RQ6"},
    {"riskID": "RK07", "riskTitle": "Supplier bushing quality", "riskDescription": "Incoming bushing defects", "riskCategory": "Threat", "riskSeverity": 4, "riskLikelihood": 2, "riskOwner": person_by_role["R09"], "riskStatus": "Closed", "riskCreatedAt": "2026-04-01T09:00:00", "riskReviewedAt": "2026-08-01T09:00:00", "eventID": None, "requirementID": "RQ5"},
    {"riskID": "RK08", "riskTitle": "Faster offer turnaround", "riskDescription": "Automation opportunity in offer calc", "riskCategory": "Opportunity", "riskSeverity": 2, "riskLikelihood": 5, "riskOwner": person_by_role["R08"], "riskStatus": "Open", "riskCreatedAt": "2026-06-01T09:00:00", "riskReviewedAt": None, "eventID": "E1", "requirementID": "RQ7"},
    {"riskID": "RK09", "riskTitle": "Noise limit breach", "riskDescription": "Urban site acoustic risk", "riskCategory": "Threat", "riskSeverity": 3, "riskLikelihood": 2, "riskOwner": person_by_role["R05"], "riskStatus": "Accepted", "riskCreatedAt": "2026-06-05T09:00:00", "riskReviewedAt": "2026-09-05T09:00:00", "eventID": "E2", "requirementID": "RQ3"},
    {"riskID": "RK10", "riskTitle": "Documentation traceability gap", "riskDescription": "Audit findings on records", "riskCategory": "Threat", "riskSeverity": 2, "riskLikelihood": 3, "riskOwner": person_by_role["R09"], "riskStatus": "Closed", "riskCreatedAt": "2026-03-10T09:00:00", "riskReviewedAt": "2026-07-10T09:00:00", "eventID": None, "requirementID": "RQ4"},
]

# Event Log — status transitions with timestamps covering all resolution buckets.
# Buckets are derived (resolved - opened): <1h, 1-8h, 8-24h, 1-7d, >7d.
event_log = []
_log_seq = 1
_log_specs = [
    # eventID, opened_ts, resolved_ts, changedByRole, note
    ("E1", "2026-05-02T09:00:00", "2026-05-02T09:40:00", "R08", "Auto-resolved by planner"),      # <1h
    ("E2", "2026-05-06T10:30:00", "2026-05-06T15:30:00", "R02", "Resolved same day"),               # 1-8h
    ("E3", "2026-05-09T14:00:00", "2026-05-10T10:00:00", "R10", "Overnight review"),                # 8-24h
    ("E4", "2026-05-14T08:15:00", "2026-05-18T08:15:00", "R09", "Investigation took days"),         # 1-7d
    ("E5", "2026-05-20T11:45:00", "2026-06-05T11:45:00", "R07", "Long study"),                      # >7d
    ("E6", "2026-05-25T16:20:00", "2026-05-26T09:20:00", "R02", "Next-morning change"),             # 8-24h
]
for ev, opened, resolved, role, note in _log_specs:
    uid = person_by_role[role]
    event_log.append({"logID": "LG%03d" % _log_seq, "eventID": ev, "previousStatus": None, "newStatus": "Open", "changedAt": opened, "changedBy": uid, "changeNote": "Event opened"})
    _log_seq += 1
    event_log.append({"logID": "LG%03d" % _log_seq, "eventID": ev, "previousStatus": "Open", "newStatus": "InProgress", "changedAt": opened, "changedBy": uid, "changeNote": "Work started"})
    _log_seq += 1
    event_log.append({"logID": "LG%03d" % _log_seq, "eventID": ev, "previousStatus": "InProgress", "newStatus": "Resolved", "changedAt": resolved, "changedBy": uid, "changeNote": note})
    _log_seq += 1

# ----------------------------------------------------------------------------
# Control (query views) — generated consistent with Jobs/Tasks/Forecasts.
# Stored with human-readable grouping labels (Departments not modeled).
# ----------------------------------------------------------------------------
fn_name = {f["functionID"]: f["functionName"] for f in functions}
role_name = {r["roleID"]: r["roleName"] for r in roles}

# Capacity: per role for the Q4-2026 window. availableHours from role headcount;
# allocatedHours summed from task execution linked via tickets in the window.
capacity = []
_cap_seq = 1
# allocated per role from tickets whose resolutionTime falls in 2026-09..2027-01
_alloc = {}
for t in tickets:
    if t["resolutionTime"] and "2026-09" <= t["resolutionTime"][:7] <= "2027-01":
        for taskID in combo_tasks[combo_by_ticket[t["ticketID"]]]:
            task = next(tk for tk in tasks if tk["taskID"] == taskID)
            _alloc[task["roleID"]] = _alloc.get(task["roleID"], 0) + task["executionTime"]
for r in roles:
    avail = r["quantity"] * 160  # ~160 productive hours per head per period
    alloc = _alloc.get(r["roleID"], 0)
    capacity.append({
        "capacityID": "CAP%02d" % _cap_seq,
        "roleID": r["roleID"], "roleName": r["roleName"],
        "functionName": fn_name[r["functionID"]],
        "factoryID": "FC1",
        "periodType": "Quarter", "periodYear": 2026, "periodQuarter": 4, "periodMonth": None,
        "periodStart": "2026-09", "periodFinish": "2027-01",
        "availableHours": avail, "allocatedHours": alloc,
    })
    _cap_seq += 1

# Usage: per function per month from Jobs realExecutionTime.
usage = []
_use_seq = 1
person_fn = {p["userID"]: p["functionID"] for p in people}
person_squad = {p["userID"]: p["squadID"] for p in people}
usage_acc = {}   # (functionID, month) -> hours
for j in jobs:
    if not j["realEndDate"] or not j["realExecutionTime"]:
        continue
    month = j["realEndDate"][:7]
    fid = person_fn[j["userID"]]
    usage_acc[(fid, month)] = usage_acc.get((fid, month), 0) + j["realExecutionTime"]
for (fid, month), hrs in sorted(usage_acc.items()):
    y, m = month.split("-")
    usage.append({
        "usageID": "USG%03d" % _use_seq,
        "regionID": "EMEA", "departmentID": fid,
        "functionName": fn_name[fid], "customerName": None, "squadName": None,
        "periodType": "Month", "periodYear": int(y), "periodMonth": int(m),
        "usedHours": hrs,
        "plannedHours": round(hrs * 0.9, 1),
        "reportedAt": month + "-28T17:00:00", "reportedBy": person_by_role["R08"],
    })
    _use_seq += 1

# Productivity: per team(function) per month spanning all efficiency buckets.
productivity = []
_prd_seq = 1
_prod_specs = [
    # teamFunctionID, month, output, target  -> efficiency buckets <80 / 80-100 / >100
    ("F1", 10, 700, 800),   # 87.5%
    ("F2", 10, 900, 850),   # 105.9%
    ("F3", 10, 500, 700),   # 71.4%
    ("F4", 10, 320, 300),   # 106.7%
    ("F5", 10, 180, 240),   # 75%
    ("F1", 11, 780, 800),   # 97.5%
    ("F2", 11, 820, 850),   # 96.5%
    ("F3", 11, 620, 700),   # 88.6%
]
for fid, month, out, tgt in _prod_specs:
    productivity.append({
        "productivityID": "PRD%02d" % _prd_seq,
        "teamID": fid, "teamName": fn_name[fid],
        "factoryID": "FC1",
        "periodType": "Month", "periodYear": 2026, "periodMonth": month,
        "output": out, "target": tgt,
    })
    _prd_seq += 1

# ----------------------------------------------------------------------------
# Assemble
# ----------------------------------------------------------------------------
dataset = {
    "_meta": {
        "description": "EDQMS Global Engineering Portal — mockup demo dataset. Base (user-entered) fields only; computed/mirror/rollup fields are recomputed by validate_mockup.py.",
        "generated_by": "build_mockup_data.py",
        "schema": "datamodel.json",
    },
    "Customers": {
        "Factories": factories,
        "Forecasts": forecasts,
        "Forecast Scopes": forecast_scopes,
    },
    "Operation": {
        "Tasks": tasks,
        "Events": events,
        "Processes": processes,
        "Activities": activities,
        "Workflows": workflows,
        "Actions": actions,
        "Constraint Types": constraint_types,
        "Constraints": constraints,
        "Handouts": handouts,
        "Channels": channels,
    },
    "Inventory": {
        "Product Scopes": product_scopes,
        "Scopes": scopes,
        "Products": products,
        "Product Class": product_class,
        "Product Groups": product_groups,
    },
    "Workload": {
        "Tickets": tickets,
        "Projects": projects,
        "Jobs": jobs,
    },
    "Control": {
        "Capacity": capacity,
        "Usage": usage,
        "Productivity": productivity,
    },
    "Talent": {
        "Squads": squads,
        "Roles": roles,
        "Skill Levels": skill_levels,
        "Functions": functions,
        "Graduation": graduation,
        "Competence": competence,
        "People": people,
        "Onboarding": onboarding,
    },
    "Quality": {
        "Risks": risks,
        "Sources": sources,
        "Source Categories": source_categories,
        "Requirements": requirements,
        "actionApplication": action_application,
        "Event Log": event_log,
    },
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mockup_data_prototype.json")
    with open(out, "w") as fh:
        json.dump(dataset, fh, indent=2, ensure_ascii=False)
    counts = {m: {t: len(rows) for t, rows in tables.items()} for m, tables in dataset.items() if m != "_meta"}
    total = sum(len(rows) for m, tables in dataset.items() if m != "_meta" for rows in tables.values())
    print("Wrote", out)
    print("Total records:", total)
    for m, tabs in counts.items():
        print(" ", m + ":", ", ".join("%s=%d" % (k, v) for k, v in tabs.items()))
