#!/usr/bin/env python3
"""
validate_mockup.py — proves mockup_data_prototype.json is relationally sound and
that every report defined in datamodel.json is actually buildable from it.

Two phases:
  1) Referential integrity — every FK / FK-list resolves to an existing record.
  2) Report feasibility — each non-null Report-* rule in datamodel.json is
     recomputed from the base data and marked PASS (non-empty, sensible result)
     or FAIL.

Run:  python3 validate_mockup.py
Exit code 0 = all green, 1 = at least one failure.
"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "mockup_data_prototype.json")))


def tbl(module, table):
    return DATA[module][table]


# Flatten helpers -------------------------------------------------------------
def index(rows, pk):
    return {r[pk]: r for r in rows}


factories = tbl("Customers", "Factories")
forecasts = tbl("Customers", "Forecasts")
forecast_scopes = tbl("Customers", "Forecast Scopes")
tasks = tbl("Operation", "Tasks")
events = tbl("Operation", "Events")
processes = tbl("Operation", "Processes")
activities = tbl("Operation", "Activities")
workflows = tbl("Operation", "Workflows")
actions = tbl("Operation", "Actions")
constraint_types = tbl("Operation", "Constraint Types")
constraints = tbl("Operation", "Constraints")
handouts = tbl("Operation", "Handouts")
channels = tbl("Operation", "Channels")
product_scopes = tbl("Inventory", "Product Scopes")
scopes = tbl("Inventory", "Scopes")
products = tbl("Inventory", "Products")
product_class = tbl("Inventory", "Product Class")
product_groups = tbl("Inventory", "Product Groups")
tickets = tbl("Workload", "Tickets")
projects = tbl("Workload", "Projects")
jobs = tbl("Workload", "Jobs")
capacity = tbl("Control", "Capacity")
usage = tbl("Control", "Usage")
productivity = tbl("Control", "Productivity")
squads = tbl("Talent", "Squads")
roles = tbl("Talent", "Roles")
skill_levels = tbl("Talent", "Skill Levels")
functions = tbl("Talent", "Functions")
graduation = tbl("Talent", "Graduation")
competence = tbl("Talent", "Competence")
people = tbl("Talent", "People")
onboarding = tbl("Talent", "Onboarding")
risks = tbl("Quality", "Risks")
sources = tbl("Quality", "Sources")
source_categories = tbl("Quality", "Source Categories")
requirements = tbl("Quality", "Requirements")
action_application = tbl("Quality", "actionApplication")
event_log = tbl("Quality", "Event Log")

# id sets / maps
F = index(factories, "factoryID")
PEOPLE = index(people, "userID")
ROLE = index(roles, "roleID")
FUNC = index(functions, "functionID")
SL = index(skill_levels, "skillLevelID")
EV = index(events, "eventID")
PROC = index(processes, "processID")
ACT = index(activities, "activityID")
WF = index(workflows, "workflowID")
PS = index(product_scopes, "productScopeID")
PG = index(product_groups, "productGroupID")
SC = index(scopes, "scopeID")
PRODUCT = index(products, "productID")
FS = index(forecast_scopes, "forecastScopeID")
FO = index(forecasts, "forecastID")
TASK = index(tasks, "taskID")
TICKET = index(tickets, "ticketID")
PROJ = index(projects, "projectID")
CMP = index(competence, "competenceID")
RISK = index(risks, "riskID")
SRC = index(sources, "sourceID")
REQ = index(requirements, "requirementID")

# ---------------------------------------------------------------------------
# Phase 1: referential integrity
# ---------------------------------------------------------------------------
errors = []


def check_fk(rows, field, target, label, nullable=True, is_list=False):
    ids = set(target.keys()) if isinstance(target, dict) else set(target)
    for r in rows:
        v = r.get(field)
        if v is None or v == [] or v == "":
            if not nullable:
                errors.append("%s: %s is required but empty" % (label, field))
            continue
        vals = v if is_list else [v]
        for x in vals:
            if x not in ids:
                errors.append("%s.%s -> %r not found" % (label, field, x))


check_fk(forecasts, "factoryID", F, "Forecasts", nullable=False)
check_fk(forecasts, "createdBy", PEOPLE, "Forecasts")
check_fk(forecast_scopes, "forecastID", FO, "ForecastScopes", nullable=False)
check_fk(forecast_scopes, "productScopeID", PS, "ForecastScopes", nullable=False)
check_fk(forecast_scopes, "eventID", EV, "ForecastScopes", nullable=False)

check_fk(tasks, "eventID", EV, "Tasks", nullable=False)
check_fk(tasks, "processID", PROC, "Tasks", nullable=False)
check_fk(tasks, "activityID", ACT, "Tasks", nullable=False)
check_fk(tasks, "actionID", index(actions, "actionID"), "Tasks", nullable=False)
check_fk(tasks, "productScopeID", PS, "Tasks")
check_fk(tasks, "roleID", ROLE, "Tasks", nullable=False)
check_fk(tasks, "constrainIDs", index(constraints, "constrainID"), "Tasks", is_list=True)
check_fk(tasks, "taskInputID", index(handouts, "handoutID"), "Tasks")
check_fk(tasks, "taskOutputID", index(handouts, "handoutID"), "Tasks")
check_fk(tasks, "customerName", F, "Tasks")
check_fk(tasks, "parentStepID", WF, "Tasks")

check_fk(events, "sourceID", SRC, "Events")
check_fk(processes, "processOwner", PEOPLE, "Processes")
check_fk(processes, "parentProcessID", PROC, "Processes")
check_fk(activities, "processID", PROC, "Activities", nullable=False)
check_fk(activities, "roleID", ROLE, "Activities", nullable=False)
check_fk(actions, "activityID", ACT, "Actions", nullable=False)
check_fk(actions, "riskID", RISK, "Actions")
check_fk(actions, "applicationID", index(action_application, "applicationID"), "Actions")
check_fk(workflows, "processID", PROC, "Workflows", nullable=False)
check_fk(workflows, "activities", ACT, "Workflows", nullable=False)
check_fk(workflows, "parentStepID", WF, "Workflows")
check_fk(constraints, "constrainTypeID", index(constraint_types, "constrainTypeID"), "Constraints", nullable=False)
check_fk(handouts, "channelID", index(channels, "channelID"), "Handouts", nullable=False)

check_fk(product_scopes, "productGroupID", PG, "ProductScopes", nullable=False)
check_fk(product_scopes, "scopeID", SC, "ProductScopes", nullable=False)
check_fk(product_groups, "products", PRODUCT, "ProductGroups", nullable=False)
check_fk(product_groups, "productClassID", index(product_class, "productClassID"), "ProductGroups", is_list=True)

check_fk(tickets, "projectID", PROJ, "Tickets", nullable=False)
check_fk(tickets, "customerName", F, "Tickets", nullable=False)
check_fk(tickets, "eventID", EV, "Tickets", nullable=False)
check_fk(tickets, "forecastScopeID", FS, "Tickets", nullable=False)
check_fk(tickets, "ticketOwner", PEOPLE, "Tickets")
check_fk(tickets, "escalatedToEventID", EV, "Tickets")
check_fk(projects, "customerName", F, "Projects", nullable=False)
check_fk(projects, "projectOwner", PEOPLE, "Projects")
check_fk(jobs, "ticketID", TICKET, "Jobs", nullable=False)
check_fk(jobs, "taskID", TASK, "Jobs", nullable=False)
check_fk(jobs, "userID", PEOPLE, "Jobs", nullable=False)
check_fk(jobs, "predecesorJob", index(jobs, "jobID"), "Jobs")

check_fk(people, "location", F, "People", nullable=False)
check_fk(people, "functionID", FUNC, "People", nullable=False)
check_fk(people, "roleID", ROLE, "People", nullable=False)
check_fk(people, "squadID", index(squads, "squadID"), "People")
check_fk(roles, "functionID", FUNC, "Roles", nullable=False)
check_fk(roles, "skillLevelID", SL, "Roles", nullable=False)
check_fk(roles, "graduationID", index(graduation, "graduationID"), "Roles", nullable=False)
check_fk(competence, "roleID", ROLE, "Competence", nullable=False)
check_fk(competence, "scopeID", SC, "Competence", nullable=False)
check_fk(competence, "productID", PRODUCT, "Competence", nullable=False)
check_fk(competence, "skillLevelID", SL, "Competence", nullable=False)
check_fk(onboarding, "userID", PEOPLE, "Onboarding", nullable=False)
check_fk(onboarding, "competenceID", CMP, "Onboarding", nullable=False)

check_fk(risks, "riskOwner", PEOPLE, "Risks")
check_fk(risks, "eventID", EV, "Risks")
check_fk(risks, "requirementID", REQ, "Risks")
check_fk(sources, "sourceCategoryID", index(source_categories, "sourceCategoryID"), "Sources", nullable=False)
check_fk(sources, "sourceOwner", PEOPLE, "Sources")
check_fk(requirements, "sourceID", SRC, "Requirements", nullable=False)
check_fk(requirements, "productID", PRODUCT, "Requirements")
check_fk(event_log, "eventID", EV, "EventLog", nullable=False)
check_fk(event_log, "changedBy", PEOPLE, "EventLog")

check_fk(capacity, "roleID", ROLE, "Capacity", nullable=False)
check_fk(capacity, "factoryID", F, "Capacity")
check_fk(productivity, "factoryID", F, "Productivity")

# ---------------------------------------------------------------------------
# Derivations shared by reports
# ---------------------------------------------------------------------------
def role_level(roleID):
    return SL[ROLE[roleID]["skillLevelID"]]["levelRank"]


def role_function_name(roleID):
    return FUNC[ROLE[roleID]["functionID"]]["functionName"]


def fs_tasks(fs):
    """Tasks matching a forecast scope: same event AND same product scope."""
    return [t for t in tasks if t["eventID"] == fs["eventID"] and t["productScopeID"] == fs["productScopeID"]]


def ticket_tasks(tk):
    fs = FS[tk["forecastScopeID"]]
    return fs_tasks(fs)


def fs_estimated_hours(fs):
    return sum(t["executionTime"] for t in fs_tasks(fs))


def event_processes(eventID):
    return sorted({t["processID"] for t in tasks if t["eventID"] == eventID})


def open_tickets():
    return [t for t in tickets if t["ticketStatus"] in ("Open", "InProgress", "Escalated")]


# ---------------------------------------------------------------------------
# Phase 2: report feasibility
# ---------------------------------------------------------------------------
results = []


def report(name, ok, detail):
    results.append((name, ok, detail))


# ---- Customers -------------------------------------------------------------
by_region = defaultdict(int)
for f in factories:
    by_region[f["region"]] += 1
report("Factories / Report-A (donut: count by region)", len(by_region) >= 2, dict(by_region))

fac_summary = []
for f in factories:
    fac_summary.append({
        "factory": f["factoryName"],
        "activeForecasts": sum(1 for fo in forecasts if fo["factoryID"] == f["factoryID"] and fo["status"] != "Archived"),
        "openTickets": sum(1 for t in open_tickets() if t["customerName"] == f["factoryID"]),
        "activeProjects": sum(1 for p in projects if p["customerName"] == f["factoryID"] and p["projectStatus"] != "Closed"),
        "region": f["region"],
    })
report("Factories / Report-B (table: factory summary)", len(fac_summary) == len(factories), fac_summary[:2])

# Forecasts Report-A: totalEstimatedHours by period, series per factory
fo_series = defaultdict(dict)
for fo in forecasts:
    total = sum(fs_estimated_hours(fs) for fs in forecast_scopes if fs["forecastID"] == fo["forecastID"])
    fo_series[F[fo["factoryID"]]["factoryName"]][fo["periodStart"]] = total
report("Forecasts / Report-A (line: totalEstimatedHours by period per factory)",
       any(any(v > 0 for v in per.values()) for per in fo_series.values()), dict(fo_series))

# Forecast Scopes Report-A: estimatedHours by productScope stacked by role
fsA = defaultdict(lambda: defaultdict(int))
for fs in forecast_scopes:
    for t in fs_tasks(fs):
        fsA[fs["productScopeID"]][ROLE[t["roleID"]]["roleName"]] += t["executionTime"]
report("Forecast Scopes / Report-A (stacked_bar: hours by scope, stacked by role)",
       any(fsA.values()), {k: dict(v) for k, v in list(fsA.items())[:2]})

# Forecast Scopes Report-B: count by region (via forecast -> factory)
fsB = defaultdict(int)
for fs in forecast_scopes:
    region = F[FO[fs["forecastID"]]["factoryID"]]["region"]
    fsB[region] += 1
report("Forecast Scopes / Report-B (bar: count by region via parent forecast factory)",
       len(fsB) >= 2, dict(fsB))

# ---- Operation -------------------------------------------------------------
tasksA = defaultdict(int)
for t in tasks:
    tasksA[PROC[t["processID"]]["processName"]] += 1
report("Tasks / Report-A (bar: count by process)", len(tasksA) >= 2, dict(tasksA))

# Tasks Report-B: top-10 execution gaps (job.real - task.planned), largest overrun first
gaps = []
for j in jobs:
    if j.get("realExecutionTime") is None:
        continue
    planned = TASK[j["taskID"]]["executionTime"]
    gaps.append({"job": j["jobID"], "task": j["taskID"], "gap": round(j["realExecutionTime"] - planned, 1)})
gaps.sort(key=lambda x: x["gap"], reverse=True)
report("Tasks / Report-B (bar: top-10 execution gaps)", len(gaps) >= 10, gaps[:10])

# Events Report-A: open ticket count by event, per factory
evA = defaultdict(lambda: defaultdict(int))
for t in open_tickets():
    evA[EV[t["eventID"]]["eventTitle"]][F[t["customerName"]]["factoryName"]] += 1
report("Events / Report-A (bar: open tickets by event per factory)", len(evA) >= 1,
       {k: dict(v) for k, v in evA.items()})

# Processes Report-A: count of tasks by processName
procA = defaultdict(int)
for t in tasks:
    procA[PROC[t["processID"]]["processName"]] += 1
report("Processes / Report-A (bar: task count by process name)", len(procA) >= 2, dict(procA))

# ---- Inventory: no reports --------------------------------------------------

# ---- Workload --------------------------------------------------------------
tkA = defaultdict(int)
for t in tickets:
    tkA[F[t["customerName"]]["factoryName"]] += 1
report("Tickets / Report-A (bar: count by customer)", len(tkA) >= 2, dict(tkA))

tkB = defaultdict(int)
for t in tickets:
    fs = FS[t["forecastScopeID"]]
    scope_name = SC[PS[fs["productScopeID"]]["scopeID"]]["scopeName"]
    tkB[scope_name] += 1
report("Tickets / Report-B (donut: count by scope)", len(tkB) >= 2, dict(tkB))

# Projects Report-A: estimated (tasks) vs real (jobs) per project
projA = []
for p in projects:
    ptickets = [t for t in tickets if t["projectID"] == p["projectID"]]
    est = sum(TASK[j["taskID"]]["executionTime"] for t in ptickets for j in jobs if j["ticketID"] == t["ticketID"])
    real = sum((j.get("realExecutionTime") or 0) for t in ptickets for j in jobs if j["ticketID"] == t["ticketID"])
    projA.append({"project": p["projectName"], "estimated": est, "real": real})
report("Projects / Report-A (bar: estimated vs real per project)",
       any(r["estimated"] > 0 for r in projA), projA[:3])

# Jobs Report-A: count Done by week (realEndDate week)
jobA = defaultdict(int)
for j in jobs:
    if j["jobStatus"] == "Done" and j.get("realEndDate"):
        jobA[j["realEndDate"][:7]] += 1
report("Jobs / Report-A (line: Done count by week/month)", len(jobA) >= 2, dict(jobA))

# Jobs Report-B: SUM(realExecutionTime) by role
jobB = defaultdict(float)
for j in jobs:
    if j.get("realExecutionTime"):
        jobB[PEOPLE[j["userID"]]["roleID"]] += j["realExecutionTime"]
jobB_named = {ROLE[k]["roleName"]: v for k, v in jobB.items()}
report("Jobs / Report-B (bar: sum realExecutionTime by role)", len(jobB) >= 2, jobB_named)

# ---- Control ---------------------------------------------------------------
capA = [{"role": c["roleName"], "available": c["availableHours"], "allocated": c["allocatedHours"]} for c in capacity]
report("Capacity / Report-A (bar: available vs allocated by role)",
       any(c["allocated"] > 0 for c in capA) and all(c["available"] > 0 for c in capA), capA[:4])

capB = {}
for c in capacity:
    if c["availableHours"]:
        capB.setdefault(c["functionName"], []).append(100.0 * c["allocatedHours"] / c["availableHours"])
capB = {k: round(sum(v) / len(v), 1) for k, v in capB.items()}
report("Capacity / Report-B (bar: utilization % by function)", len(capB) >= 2, capB)

useA = defaultdict(lambda: defaultdict(float))
for u in usage:
    useA[u["functionName"]]["%d-%02d" % (u["periodYear"], u["periodMonth"])] += u["usedHours"]
report("Usage / Report-A (line: usedHours by period per function)", len(useA) >= 2,
       {k: dict(v) for k, v in list(useA.items())[:2]})

# Usage Report-B: heatmap role x jobs count
useB = defaultdict(int)
for j in jobs:
    useB[PEOPLE[j["userID"]]["roleID"]] += 1
useB_named = {ROLE[k]["roleName"]: v for k, v in useB.items()}
report("Usage / Report-B (heatmap: job count by role)", len(useB) >= 3, useB_named)

# Productivity Report-A: teams by efficiency bucket
buckets = {"<80%": 0, "80-100%": 0, ">100%": 0}
for p in productivity:
    eff = 100.0 * p["output"] / p["target"]
    if eff < 80:
        buckets["<80%"] += 1
    elif eff <= 100:
        buckets["80-100%"] += 1
    else:
        buckets[">100%"] += 1
report("Productivity / Report-A (donut: teams by efficiency bucket)",
       all(v > 0 for v in buckets.values()), buckets)

# Productivity Report-C: oversized tasks (assigned role rank > min certified rank for scope+product)
def certified_min_rank(scopeID, productID):
    ranks = []
    for c in competence:
        if c["scopeID"] == scopeID and c["productID"] == productID:
            # is any person certified for this competence?
            if any(o["competenceID"] == c["competenceID"] and o["isCertified"] for o in onboarding):
                ranks.append(role_level(c["roleID"]))
    return min(ranks) if ranks else None


oversized = defaultdict(int)
oversized_examples = []
for t in tasks:
    ps = PS.get(t["productScopeID"])
    if not ps:
        continue
    scopeID = ps["scopeID"]
    productID = PG[ps["productGroupID"]]["products"]
    minrank = certified_min_rank(scopeID, productID)
    if minrank is not None and role_level(t["roleID"]) > minrank:
        oversized[PROC[t["processID"]]["processName"]] += 1
        if len(oversized_examples) < 4:
            oversized_examples.append({"task": t["taskID"], "role": ROLE[t["roleID"]]["roleName"],
                                       "rank": role_level(t["roleID"]), "minCertifiedRank": minrank})
report("Productivity / Report-C (bar: oversized tasks by process)", sum(oversized.values()) >= 1,
       {"byProcess": dict(oversized), "examples": oversized_examples})

# Productivity Report-D: marginal productivity — adding 1 head of a role to a process
def marginal_gain(processID, roleID, extra=1):
    ptasks = [t for t in tasks if t["processID"] == processID and t["roleID"] == roleID]
    load = sum(t["executionTime"] for t in ptasks)
    if load == 0:
        return None
    heads = max(1, ROLE[roleID]["quantity"])
    makespan_before = load / heads
    makespan_after = load / (heads + extra)
    return round(makespan_before - makespan_after, 2)


mg = marginal_gain("PR1", "R04", 1)
report("Productivity / Report-D (line: marginal gain adding a role)", mg is not None and mg > 0,
       {"process": "PR1", "role": "R04", "extraHead": 1, "makespanReductionHours": mg})

# ---- Talent ----------------------------------------------------------------
rolesA = defaultdict(int)
for r in roles:
    rolesA[FUNC[r["functionID"]]["functionName"]] += r["quantity"]
report("Roles / Report-A (donut: headcount by function)", len(rolesA) >= 3, dict(rolesA))

# Roles Report-B: task count by role where headcount>0
task_by_role = defaultdict(int)
for t in tasks:
    task_by_role[t["roleID"]] += 1
rolesB = {ROLE[k]["roleName"]: v for k, v in task_by_role.items() if ROLE[k]["quantity"] > 0}
report("Roles / Report-B (donut: tasks by role, headcount>0)", len(rolesB) >= 2, rolesB)

slA = defaultdict(int)
for r in roles:
    slA[SL[r["skillLevelID"]]["levelName"]] += r["quantity"]
report("Skill Levels / Report-A (bar: headcount by level)", len(slA) >= 2, dict(slA))

fnA = defaultdict(int)
for r in roles:
    fnA[FUNC[r["functionID"]]["functionName"]] += r["quantity"]
report("Functions / Report-A (bar: headcount by function)", len(fnA) >= 3, dict(fnA))

gradA = defaultdict(int)
for r in roles:
    gradA[index(graduation, "graduationID")[r["graduationID"]]["field"]] += r["quantity"]
report("Graduation / Report-A (donut: headcount by field)", len(gradA) >= 1, dict(gradA))

# Competence Report-A: role x scope heatmap = % required competences certified
comp_cert = {}
for o in onboarding:
    comp_cert.setdefault(o["competenceID"], []).append(o["isCertified"])
heat = defaultdict(dict)
for c in competence:
    if not c["isRequired"]:
        continue
    role_name = ROLE[c["roleID"]]["roleName"]
    scope_name = SC[c["scopeID"]]["scopeName"]
    certs = comp_cert.get(c["competenceID"], [])
    pct = round(100.0 * sum(1 for x in certs if x) / len(certs), 0) if certs else 0
    heat[role_name][scope_name] = pct
report("Competence / Report-A (heatmap: role x scope certified %)", len(heat) >= 3,
       {k: v for k, v in list(heat.items())[:3]})

peopleA = defaultdict(int)
for p in people:
    if p["isActive"]:
        peopleA[FUNC[p["functionID"]]["functionName"]] += 1
report("People / Report-A (bar: active people by function)", len(peopleA) >= 3, dict(peopleA))

# ---- Quality ---------------------------------------------------------------
riskA = [{"x": r["riskLikelihood"], "y": r["riskSeverity"], "rpn": r["riskSeverity"] * r["riskLikelihood"],
          "cat": r["riskCategory"]} for r in risks]
report("Risks / Report-A (scatter: likelihood x severity, size RPN)",
       len(riskA) >= 5 and any(r["cat"] == "Opportunity" for r in riskA) and any(r["cat"] == "Threat" for r in riskA),
       riskA[:3])

riskB = []
for r in risks:
    if r["riskStatus"] in ("Open", "UnderTreatment"):
        riskB.append({"title": r["riskTitle"], "rpn": r["riskSeverity"] * r["riskLikelihood"],
                      "actions": sum(1 for a in actions if a.get("riskID") == r["riskID"])})
report("Risks / Report-B (table: open risk register with action count)",
       len(riskB) >= 3 and any(x["actions"] > 0 for x in riskB), riskB[:4])

srcA = defaultdict(int)
for e in events:
    if e.get("sourceID"):
        cat = index(source_categories, "sourceCategoryID")[SRC[e["sourceID"]]["sourceCategoryID"]]["sourceCategoryName"]
        srcA[cat] += 1
report("Sources / Report-A (bar: events by source category)", len(srcA) >= 2, dict(srcA))

srcB = []
for s in sources:
    ev_ids = [e["eventID"] for e in events if e.get("sourceID") == s["sourceID"]]
    rks = [r for r in risks if r.get("eventID") in ev_ids]
    srcB.append({"source": s["sourceName"], "events": len(ev_ids), "risks": len(rks),
                 "openRisks": sum(1 for r in rks if r["riskStatus"] in ("Open", "UnderTreatment"))})
report("Sources / Report-B (table: source -> event -> risk traceability)",
       any(x["events"] > 0 and x["risks"] > 0 for x in srcB), srcB[:4])

reqA = defaultdict(int)
for r in requirements:
    reqA[r["requirementType"]] += 1
report("Requirements / Report-A (donut: count by type)", len(reqA) >= 2, dict(reqA))

reqB = []
for req in requirements:
    rks = [r for r in risks if r.get("requirementID") == req["requirementID"]]
    reqB.append({"requirement": req["requirementName"], "risks": len(rks),
                 "highestRPN": max([r["riskSeverity"] * r["riskLikelihood"] for r in rks], default=0)})
report("Requirements / Report-B (table: requirement-to-risk compliance)",
       any(x["risks"] > 0 for x in reqB), reqB[:4])

# Event Log Report-A: resolution time buckets
import datetime as dt


def parse(ts):
    return dt.datetime.fromisoformat(ts)


opened = {}
resolved = {}
for lg in event_log:
    if lg["newStatus"] == "Open":
        opened[lg["eventID"]] = parse(lg["changedAt"])
    if lg["newStatus"] == "Resolved":
        resolved[lg["eventID"]] = parse(lg["changedAt"])
buckets2 = {"<1h": 0, "1-8h": 0, "8-24h": 0, "1-7d": 0, ">7d": 0}
for ev_id, rt in resolved.items():
    if ev_id not in opened:
        continue
    hrs = (rt - opened[ev_id]).total_seconds() / 3600.0
    if hrs < 1:
        buckets2["<1h"] += 1
    elif hrs < 8:
        buckets2["1-8h"] += 1
    elif hrs < 24:
        buckets2["8-24h"] += 1
    elif hrs < 24 * 7:
        buckets2["1-7d"] += 1
    else:
        buckets2[">7d"] += 1
report("Event Log / Report-A (bar: resolution-time buckets)",
       sum(buckets2.values()) >= 5 and sum(1 for v in buckets2.values() if v > 0) >= 3, buckets2)

elB = [lg for lg in event_log if lg["eventID"] == "E1"]
report("Event Log / Report-B (table: audit trail for an event)", len(elB) >= 2,
       [{"from": x["previousStatus"], "to": x["newStatus"], "at": x["changedAt"]} for x in elB])

# ---------------------------------------------------------------------------
# Capacity Report-A scenario spot-check (dashboard-reports-analysis.md)
# ---------------------------------------------------------------------------
scenario_ok = True
scenario_detail = {}
try:
    t001 = TICKET["001"]
    stasks = ticket_tasks(t001)
    total = sum(t["executionTime"] for t in stasks)
    ids = sorted(t["taskID"] for t in stasks)
    scenario_detail = {
        "ticket": "001", "event": EV[t001["eventID"]]["eventTitle"],
        "resolutionTime": t001["resolutionTime"], "taskIDs": ids,
        "sumExecutionHours": total,
        "roles": sorted({ROLE[t["roleID"]]["roleName"] for t in stasks}),
    }
    scenario_ok = ids == ["012", "032", "033", "045"] and total == 36
except Exception as e:  # noqa
    scenario_ok = False
    scenario_detail = {"error": str(e)}
report("Capacity Report-A SCENARIO spot-check (tasks 012/032/033/045 = 36h)", scenario_ok, scenario_detail)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print("=" * 78)
print("PHASE 1 — REFERENTIAL INTEGRITY")
print("=" * 78)
if errors:
    for e in errors:
        print("  FAIL:", e)
    print("\n%d integrity error(s)." % len(errors))
else:
    print("  OK — all foreign keys resolve (%d tables checked)." %
          sum(len(t) for m in DATA if m != "_meta" for t in [DATA[m]]))

print()
print("=" * 78)
print("PHASE 2 — REPORT FEASIBILITY (%d reports)" % len(results))
print("=" * 78)
passed = 0
for name, ok, detail in results:
    tag = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    print("  [%s] %s" % (tag, name))
    if not ok:
        print("         detail:", json.dumps(detail, ensure_ascii=False)[:300])

print()
print("-" * 78)
print("Reports: %d/%d PASS   |   Integrity errors: %d" % (passed, len(results), len(errors)))
print("-" * 78)

if "-v" in sys.argv or "--verbose" in sys.argv:
    print("\nReport outputs (sample):")
    for name, ok, detail in results:
        print("\n%s" % name)
        print("  ", json.dumps(detail, ensure_ascii=False)[:500])

sys.exit(0 if (passed == len(results) and not errors) else 1)
