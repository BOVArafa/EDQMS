---
content-type: specification
subject:
  - dashboard
  - reports
  - datamodel
  - attributes
---

# EDQMS Dashboard Reports & Data Model Analysis

**How to use:** This document is the source specification for completing the `reports` and `filters` fields in `datamodel.json`. For each entity (table), you will find: (1) the complete attribute list including additions proposed here, (2) Report-A spec (analytical/visual chart), and (3) Report-B spec (operational/tabular list). New tables not yet in `datamodel.json` are listed at the end.

**Source diagrams:**
- LucidChart page 1 "EDQMS ER-UML" — conceptual ISO 9001:2015-aligned model
- LucidChart page 2 "Prototype-EDQMS" — implementation prototype model
- `GlobalEngineeringPortal_dashboard.html` — UI prototype (mockup); defines actual column names and report kinds per module

**ISO alignment:** all entities map to ISO 9001:2015 clauses as documented in `EDQMS-01_DataModel_DesignRationale.md`.

>[!warning] Ignore
>Para efeito de prototipo, vamos ignorar o modelo de dados de EDQMS-01_DataModel_DesignRationale.
>Considere apenas o modelo da aba prototype_EDBPM dentro do lucidChart

>[!important] Report Testing
>Voce deve verificar a necessidade de criacao de tabelas associativas ou atributos extra (mirror, rollup, PK, etc) nas tabelas existentes para garantir que os reports definidos/sugeridos sejam realmente viaveis de se construir.
>A ideia eh criar um mockup de dados para fazer esses testes que tambem servira de conteudo para as telas do prototipo.
>Os dados mockups criados para testes devem ser inseridos em um novo arquivo `mockup_data_prototype.json`

---

## Attribute Type Conventions

Every attribute in this document uses one of the following type declarations:

| Type declaration | Meaning |
|---|---|
| `PK` | Auto-generated primary key |
| `string` | Free-text input |
| `text` | Long free-text (multi-line) |
| `int` | Integer number |
| `decimal` | Decimal number |
| `bool` | True / False toggle |
| `date` | Calendar date |
| `datetime` | Date + time |
| `enum: A/B/C` | Single-select from a fixed list |
| `FK → Table (display: field)` | Lookup — user selects a record from Table; the specified field is shown in the UI |
| `rollup → Table (via: FK field)` | Computed list of child records from Table that reference this record through the given FK field |
| `computed: formula` | Value derived automatically from other fields; not user-editable |
| `multivalued` | Can hold multiple values (multi-select or tag list) |

---

## Graph Type Reference

| `graph_type` | When to use |
|---|---|
| `bar` | Counts and comparisons across categories |
| `stacked_bar` | Multi-dimension breakdown within a category |
| `line` | Trends over time (one or more series) |
| `donut` | Proportions or distribution (replaces "pie") |
| `kpi` | Single metric (count, percentage, rate) |
| `table` | Operational lists and drill-down detail |
| `scatter` | Two-axis correlation (e.g., risk severity vs. likelihood) |
| `gauge` | Utilization or capacity percentage |
| `heatmap` | Matrix views (role × scope, competence coverage) |
| `funnel` | Conversion or escalation flows |


>[!tip] Tables
>de acordo com o arquivo de referencia do prototipo (GlobalEngineeringPortal_dahsboard.html) toda tela de uma determinada tab obrigatoriamente tera uma tabela que representa a respectiva entidade do modelo de dados da tab (exemplo, tab Scopes = entidade Scope).
>Sendo assim, nao eh preciso considerar tabelas nos reports, apenas gragicos, umas vez que as tabelas sao obrigatorias em cada tela

>[!important] Rollup Columns
>Inserir por padrao em todas as tabelas, uma coluna rollup sempre que um item de uma tabela for referenciado em outra.

>[!important] Mirror Columns
>As colunas de espelho servem para 'copiar' atributos provenientes da tabela referenciada por uma coluna de rollups em novas colunas dentro da mesma tabela.
>A escolha dos atributos mirror deve ser definida de acordo com a aplicacao de relatorios ou filtros que forem definidos para a dashboard (tab)
>inserir essa tipo de coluna `mirror` em sua tabela Attribute type Conventions. as colunas mirror serao a mesma coisa que `compute: DISTINCT("table"."attribute"`.

---

## Standard Filter Keys

| `filter_key` | Type | Used in |
|---|---|---|
| `period` | date-range | Most reports |
| `periodType` | enum (Annual/Quarter/Month) | Capacity, Productivity, Usage, Forecasts |
| `owner` | FK → People | Events, Tasks, Actions, Risks |
| `factory` | FK → Factories | Forecasts, Capacity, Projects |
| `businessSegment` | enum (LPT/MT/DT) | Products, Factories |
| `status` | enum (per entity) | Events, Tasks, Actions, Risks, Tickets |
| `priority` | enum (Low/Medium/High/Critical) | Events, Tickets |
| `riskCategory` | enum (Threat/Opportunity) | Risks |
| `applicationID` | FK → actionApplication | Actions |
| `processID` | FK → Processes | Activities, Workflows |
| `scopeID` | FK → Scopes | Product Scopes, Competence |
| `productClassID` | FK → Product Class | Products, Risks |
| `roleID` | FK → Roles | Capacity, Competence, People |
| `departmentID` | FK → Department | Jobs, People, Functions |
| `locationID` | FK → Location | Jobs, Capacity, People |
| `isActive` | bool | Most registry/master-data tables |

---

## Module: Customers

### Factories

**ISO clause:** §4.1 (organisational context — internal/external environment)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `factoryID` | PK | Auto-generated primary key |
| `factoryName` | string | Short code, e.g. "PN" |
| `city` | string | |
| `country` | string | |
| `businessSegment` | enum: LPT/MT/DT | |
| `region` | enum: EMEA/Americas/APAC | Geographical grouping |
| `isActive` | bool | Soft-delete flag |
| `forecasts` | rollup → Forecasts (via: factoryID) | All forecast records belonging to this factory |

**Report-A — Factories by Region**
- `graph_type`: `donut`
- `rule`: Count of Factories grouped by `region`
- `filters`: `["businessSegment", "isActive"]`

**Report-B — Factory Summary**
- `graph_type`: `table`
- `query`: All factories with computed columns: active forecast count, open ticket count, active project count, region
- `filters`: `["businessSegment", "region", "isActive"]`

---

### Forecasts

**ISO clause:** §6.1 (planning — resource demand projection)

**Definition:** A Forecast groups a set of Forecast Scopes so that a Factory can project to global engineering its intended use of role resources for a given planning period.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `forecastID` | PK | Auto-generated primary key |
| `factoryID` | FK → Factories (display: factoryName) | Factory submitting this forecast |
| `forecastPeriod` | enum: Annual/Quarter/Month | Granularity of the period |
| `forecastYear` | int | e.g., 2026 |
| `forecastQuarter` | int (nullable) | 1–4; required when period = Quarter |
| `forecastMonth` | int (nullable) | 1–12; required when period = Month |
| `status` | enum: Draft/Submitted/Approved/Archived | |
| `createdBy` | FK → People (display: userName) | |
| `createdAt` | datetime | |
| `forecastScopes` | rollup → Forecast Scopes (via: forecastID) | All child Forecast Scope records belonging to this forecast |
| `totalEstimatedHours` | computed: SUM(forecastScopes.estimatedHours) | Total demand projected by this forecast across all scopes |


>[!bug] Attributes
>Insert:
> - periodStart: datetime (depende da condicao de `forecastPeriod`)
> - periodFinish: datetime (depende da condicao de `forecastPeriod`)

>[!warning] User Interface
>Verificar como implementar o formulario e o modelo de dados dessa tabela com cuidado. Se necessario, pode criar uma outra entidade associativa.
>No formulario do protipo, sera preciso o seguinte:
> - Se `forecastPeriod` for:
>   - month: habilitar campo `forecastMonth` para o usuario escolher o ano e o mes.
>     - periodStart: mes e ano escolhido em `forecastPeriod`
>     - periodFinish: mes e ano escolhido em `forecastPeriod`
>   - quarter: habilitar campo `forecastQuarter` para o usuario escolher o ano e o quarter 
>     - periodStart: user input -> mes e ano
>     - periodFinish: calculated -> mes e ano de `periodStart` adicionado de 4 meses a frente.
>   - Annual: habilitar campo `forecastYear` para o usuario escolher um periodo de 12 meses
>     - periodStart: user input -> mes e ano
>     - periodFinish: user input -> mes e ano

**Report-A — Forecast Volume Trend**
- `graph_type`: `line`
- `rule`: `totalEstimatedHours` plotted by period (year + quarter), one series per factory
- `filters`: `["forecastPeriod", "factoryID", "forecastYear", "status"]`

>[!note] no need for Report-B


---

### Forecast Scopes

**ISO clause:** §6.1 + §6.2 (planning with product-scope and event granularity)

**Definition:** A Forecast Scope is the atomic unit of a Forecast. It specifies one Event × Product Scope combination. The Event determines which Process is triggered and therefore which Tasks (with their roles and execution times) make up the workload. The `estimatedHours` and the `roles` involved are both computed from the Tasks that belong to the Process triggered by that Event.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `forecastScopeID` | PK | Auto-generated primary key |
| `forecastID` | FK → Forecasts (display: forecastID + period) | Parent forecast |
| `productScopeID` | FK → Product Scopes (display: scopeName + products) | Product × Scope combination |
| `eventID` | FK → Events (display: eventTitle) | Event that triggers the Process for this scope; determines which Tasks (and therefore roles and hours) are included |
| `processID` | computed: Events → Trigger → Processes (display: processName) | Process triggered by the selected Event; drives the task list |
| `tasks` | rollup → Tasks (via: eventID + productScopeID) | All Tasks that match this event and product scope; source of roles and execution times |
| `roles` | computed: DISTINCT(tasks.roles)  | Roles derived from Tasks in the triggered Process for this scope; not a direct user input |
| `estimatedHours` | computed: SUM(tasks.executionTime) | Total execution hours across all Tasks in the triggered Process for this scope |
| `notes` | text | |


>[!bug] Attributes
>no need for `estimatedCost`

**Report-A — Estimated Hours by Role per Scope**
- `graph_type`: `stacked_bar`
- `rule`: `estimatedHours` grouped by `productScopeID` (scope name), stacked by `roles`
- `filters`: `["forecastID", "period", "factory", "businessSegment"]`

**Report-B — Scope Coverage**
- `graph_type`: `bar`
- `rule`: Count of Forecast Scopes grouped by `region` (from linked Product Scope)
- `filters`: `["forecastPeriod", "factory", "businessSegment", "eventID"]`

---

## Module: Operation

### Tasks

**ISO clause:** §8 (operational execution)

**Definition:** A Task is the atomic work unit in the EDQMS. It is created when a user selects an Event + Process + Activity combination. The remaining columns (Products, Scopes, Workflow, Action, Roles) are derived from the selected Activity's Payload and Workflow associations. A Task can be escalated to an Event when it meets escalation criteria.

>[!abstract] Definition
>Uma tarefa eh a aplicacao de uma acao `action` a uma atividade de processo (`workflow`)

>[!bug] Issue 
>A tabela de tarefa servira como templates para execucao, apenas. Sera no modulo `Workload` que iremos criar os `jobs` para engenharia baseado nesses templates. Ou seja, quando um job for criado, devera ser selecionada uma tarefa e ai sim ser adicionado o `taskOwner`, `taskStatus`, `taskDueDate`, `porjectID`.
>esta tabela deve possui o atributo `parentStepID`(display `workflowName`) que sera um rollup de `workflowID`.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `taskID` | PK | Auto-generated primary key |
| `eventID` | FK → Events (display: eventTitle) | Event that triggered this task |
| `processID` | FK → Processes (display: processName) | Process this task belongs to |
| `activityID` | FK → Activities (display: activityName) | Activity this task executes |
| `products` | computed: activityID → Payload → Products (display: productName) | Products derived from the Activity's Payload; multivalued |
| `scopes` | computed: activityID → Payload → Scopes (display: scopeName) | Scopes derived from the Activity's Payload; multivalued |
| `workflowID` | computed: lookup Workflows WHERE processID + activityID match (display: workflowID) | Workflow that sequences this activity |
| `actionID` | computed: lookup Actions via activityID (display: actionName) | Action associated with this activity |
| `executionTime` | decimal | Planned execution time in hours; defaults to Activity.executionTime |
| `roles` | computed: activityID → Activity.roleID scope(display: roleName) | Roles derived from the Activity; multivalued |


>[!bug] Attributes
>Incluir:
> - `constraintName`: rollup de itens da tabela `constraints` agrupados por `constrainTypeID`.
> - `taskInput`: rollup de itens da tabela `handouts` 
> - `taskOutput`: rollup de itens da tabela `handouts`
> - `customerName`: rollup de itens da tabela `factories`
> - `processID` sera um campo calculado do atributo `eventID`. O campo de processo mostrara opcoes de processos disparados pelo evento selecionado,
> - `workflowID` sera um campo calculado do atributo `processID`. as opcoes de escolha do workflowID serao filtradas pelo match de processID.
> - `activityID` deve ser um campo calculado de `workflowID`. Ao selecionar o workflowID o activityID sera automaticamente inserido (MIRROR)
> - `ticketID`: rollup -> Tickets via taskID
> - `taskName`: CONCAT(actionName,activityName,processName)
>Update:
> - `roles`: computed: taskID -> Competence.roleID (disply: roleName)

>[!note] Future Implementation 
> Vamos ignorar a implementacao de `isEscalated` por enquanto. Essa eh um funcionladidade importante porem complexa para ser analisada no contexto do MVP.

>[!note] Consulta para planejamento
>O usuario que estiver planejando os `jobs` de engenharia deve ser capaz de consultar essa tabela para filtrar os `tasks` por:
>- scopeName
>- designType
>- productName
>- eventName
>- processName
>>[!abstract] Why?
>>Este tipo de filtragem eh importante para que a pessoa no `role` de `planner` possa identificar quais tarefas devem ser executadas quando um determinado evento for inserido em `tickets`

**Report-A — Tasks by Process**
- `graph_type`: `bar`
- `rule`: Count of Tasks grouped by `processID`
- `filters`: `["taskStatus", "owner", "eventID", "period"]`

**Report-B — Execution Hours per Workflow**
- `graph_type`: `line`
- `rule`: SUM(`executionTime`) plotted by period, one series per `workflowID`
- `filters`: `["workflowID", "processID", "period", "owner"]`

>[!tip] Report B 
>Alterar para um grafico que mostre a relacao entre `executionTime` das tarefas com `realExecutionTime` dos jobs, organizado em ordem crescente de diferenaca entre realExcution e execution time, mostrando apenas as 10 mais criticas. Usar como filtros: processName, roles, productName, scopeName

---

### Events

**ISO clause:** §9.1 (monitoring) + §10.1/10.2 (corrective action trigger) — architectural pivot of the EDQMS

>[!bug] Definitions
>Preciso definir o conceito de evento para que voce comprrenda a arquitetura. 
>Um evento eh apenas um agregador de processos, ele nao sera executado, ele dispara uma determinada execucao. Eh exatamente isso que eh definido no forecast, quais eventos e parametros de execucao (forecastScopes) um determinado forecast agrupara.
>Neste momento nao vamos nos preocupar em vincular eventos a acoes corretivas ou nao conformidades. No futuro sera desenvolvido um modulo dedicado para isto.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `eventID` | PK | Auto-generated primary key |
| `eventTitle` | string | Dynamic — set at creation |
| `eventDescription` | text | |
| `eventCreatedAt` | datetime | |
| `tasks` | rollup → Tasks (via: eventID) | All Tasks triggered by this event |
| `forecastScopes` | rollup → Forecast Scopes (via: eventID) | Forecast Scopes that use this event to estimate workload |


>[!bug] Attributes 
>rollup de processos que sao disparados pelo evento.
>rollup de tarefas existente para cada processo disparado pelo evento.
>rollup de tickets aberto para cada evento

**Report-A — Workflow Status**
- `graph_type`: `donut`
- `rule`: Count of Events grouped by `eventStatus`
- `filters`: `["period", "owner", "priority", "sourceID"]`

**Report-B — Open Events List**
- `graph_type`: `table`
- `query`: Events where `eventStatus` IN (Open, InProgress); columns: title, owner, channel, priority, age (days since createdAt), linked task count
- `filters`: `["status", "owner", "priority", "channelID"]`

>[!tip] Report
>Criar apenas um report que mostre a quantidade de tickets aberto, agrupado por `eventName`, para cada factory. Estas informacoes devem ser retiradas da coluna rollup `ticketID`
>filter: `factoryName`(including all), `productName`(including all), `scopeName`(including all).
>Insira na tabela de eventos quaisquer atributos de rollup ou pesquisa que julgue necessario para construir este report.

---

### Processes

**ISO clause:** §4.4 (QMS process approach)

>[!abstract] Definition
>A tabela de processo servira para agrupar os `workflows`. Nesta tabela o usuario apenas criara um item de processo que posteriormente sera utilizado na criacao dos steps de processo dentro da tabela `workflow`

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `processID` | PK | |
| `processName` | string | |
| `processOwner` | FK → People (display: userName) | |
| `processDescription` | text | |
| `parentProcessID` | FK → Processes (display: processName) (nullable) | Self-referential: "Sub-process of" |
| `processStatus` | enum: Active/Draft/Deprecated | |
| `targetExecutionTime` | decimal | Expected total duration in hours |
| `processVersion` | string | e.g., "v1.2" |
| `activities` | rollup → Activities (via: processID) | All Activities belonging to this Process |
| `tasks` | rollup → Tasks (via: processID) | All Tasks belonging to this Process |


>[!bug] Attributes 
>`targetExecutionTime` deve ser uma coluna rollup com a media dos tempos de execucao dos diferentes grupos das tarefas que compoe o process
>(um mesmo processo pode ter tarefas iguais - mesma acao para o mesmo workflow - mas agrupados por ecopos ou produtos distintos que impactam no tempo de execucao da tarefa) 
>ou seja, tire as medias dos tempos das tarefas para aquelas que possuirem a mesma combinacao dos atributos `action` e `workflow`. 
>Incluir um atributo `processSytemID` onde o usuario possa inserir um numero de ID de um sistema de cadastro externo como referencia. esse campo nao deve ser obrigatorio.


**Report-A — Tasks by Process**
- `graph_type`: `bar`
- `rule`: Count of Tasks grouped by `processName`
- `filters`: `["processStatus", "owner"]`

>[!tip] Report 
>Apenas o report A deve ser inserido nesta tela.
>os fitlros do report A devem ser: `productName`(including all), `scopeName`(including all), `design`(including all)
>Insira nesta tabela quaisquer atributos de rollup ou pesquisa que julgue necessario para construir este report.


---

### Activities

**ISO clause:** §4.4.1 (process sub-steps) + §7.1.6 (knowledge management via Procedures)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `activityID` | PK | |
| `activityName` | string | |
| `processID` | FK → Processes (display: processName) | Parent process |
| `roleID` | FK → Roles (display: roleName) | Role responsible for executing this activity; drives Tasks.roles |
| `procedureID` | FK → Procedures (display: procedureNumber) (nullable) | Documented execution method (ISO §7.5) |
| `tasks` | rollup → Tasks (via: activityID) | All Tasks derived from this Activity |


>[!bug] Definition 
>As atividades nao possuem tempo de execucao,owner,status, start date ou end date, pois a execucao de uma atividade sera definida na lista de `tasks`.
>O `roleID` deve vir do atributo `tasks`, pois eh na tarefa que o `role` eh definido.
>O atributo `procedureID` sera um campo de attachment na dashboard. Este campo de attachment deve permitir a insercao de um link para o documento e uma descricao do link, que deve ser o ID do procedimento.

>[!note] Sem necessidade de Reports para esta tab

---

### Workflows

**ISO clause:** §4.4.1 (sequence and interaction of processes)

>[!abstract] Definition
>A tabela de workflow eh onde serao cadastrados os steps de cada processo.
>Sera atraves da relacao dos itens desta tabela que os usuarios entenderao como um processo deve ser executado em termos de atividades.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `workflowID` | PK | Displayed as e.g., "WF-002" |
| `workflowName` | string | |
| `processID` | FK → Processes (display: processName) | |
| `activities` | rollup → Activities (via: processID) (display: activityName, multivalued) | Activities that form this workflow |
| `parentStepID` | FK → Workflows (nullable) | Self-referential step ordering |


>[!bug] Attributes
>Insert:
> - `taskID`: rollup das tarefas que utilizam o item do `workflow`
> - `inputs`: MIRROR da coluna `taskInput` determinado pelo atributo `taskID`
> - `outputs`: MIRROR da coluna `taskOutput` determinado pelo atributo `taskID`
> - `scopes`: MIRROR da coluna `scopeID` determinado pelo atributo `taskID`
> - `customer`: MIRROR da coluna `customerName` determinado pelo atributo `taskID`
> - `procedures`: MIRROR da coluna `procedureName` determinado pelo atributo `taskID`
> - `products`: MIRROR da coluna `productName` determinado pelo atributo `taskID`
> - `constraints`: MIRROR da coluna `constraintName` determinado pelo atributo `taskID`
>Update:
> - `activities`: single select, not multivalued
> - `workflowName` deve ser a concatenacao de `activityName` e `processName` e nao sera um input


>[!note] Sem necessidade de Reports para esta tab

---

### Actions

**ISO clause:** §6.1.2 (actions to address risks and opportunities) + §10.1 (improvement)

>[!abstract] Definition
>Uma `action` eh o que define o procedimento a ser realizado para execucao de um determinado step (workflow) dentro de um processo.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `actionID` | PK | |
| `actionName` | string | |
| `actionDescription` | text | |
| `activityID` | FK → Activities (display: activityName) | Activity this action belongs to |


>[!bug] Attributes
>- adicionar atributo `taskID` que deve ser um rollup das tasks que utilizam uma determinada `action`
>- `activityID`. Este atributo sera uma coluna mirror do rollup `taskID` de cada action. 


>[!tip] Filtros importantes que o modelo da tabela deve permitir
>Acrescentar atributos nesta tabela que permitam que o usuario possa filtrar as `actions` para determinar:
>- Quais acoes fazem parte de um determinado workflow (combinacao atividade + processo).
>- Quais acoes fazem parte de uma determinada atividade


>[!note] Sem necessidade de Reports para esta tab

---

### Constraints

**ISO clause:** §4.3 (scope of QMS — bounding conditions for risk treatment) 

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `constrainID` | PK | |
| `constrainName` | string | |
| `constrainDescription` | text | |
| `constrainTypeID` | FK → Constraint Types (display: constrainTypeName) | Operational / Design / Testing / Technical / Commercial |
| `isActive` | bool | |
| `regulatoryReference` | string (nullable) | e.g., IEC standard code |


>[!note] Sem necessidade de Reports para esta tab

---

### Handouts

**ISO clause:** §4.4.2(b) (retained documented information as evidence of conformity)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `handoutID` | PK | |
| `handoutName` | string | |
| `handoutDescription` | text | |
| `createdAt` | datetime | |
| `channelID` | FK → Channels (display: channelName) | Delivery channel |


>[!bug] Attributes
>Insert:
> - `taskID`: rollup with all the tasks that have the constraint assigned to it
> - Template: attachment (with a field option to insert a title for the attachment)
> - type: enum=["data", "file"]
>Eliminate:
> - `activityID`
> - `fileURL`

>[!note] Sem necessidade de Reports para esta tab

---

### Channels

**ISO clause:** §7.4 (communication — how information is distributed)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `channelID` | PK | |
| `channelName` | string | e.g., Portal, Salesforce, Outlook |
| `channelOwner` |string| e.g. Microsoft, Oracle|
| `channelStatus` | enum: Active/Inactive | |
| `handouts` | rollup → Handouts (via: channelID) | All Handouts delivered through this channel |


>[!bug] Attributes
>Eliminate:
> - `channelDescription`
> - `events`
> - `channelType`
>Update:
> - `channelOwner`: Type = text (tooltip: nome da empresa ou pessoa responsavel pela gestao do canal)

>[!note] Sem necessidade de Reports para esta tab

---

## Module: Inventory (Product Scopes)

### Product Scopes

**ISO clause:** §4.3 (scope of QMS) + §8.1 (operational planning — product-scope combinations)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `productScopeID` | PK | Displayed as a group code, e.g. "AA" |
| `productGroupID` | FK → Product Groups (display: groupCode) | e.g., "AA" |
| `scopeID` | FK → Scopes (display: scopeName) | |
| `products` | rollup → Products (via: productGroupID) (display: productName, multivalued) | Products belonging to this product group |
| `businessSegment` | enum: LPT/MT/DT | |
| `design` | enum: Siemens Energy/Partner | Design ownership |
| `isActive` | bool | |
| `createdAt` | datetime | |
| `forecastScopes` | rollup → Forecast Scopes (via: productScopeID) | |


>[!bug] Attributes
>Insert:
> - `productClassID`: MIRROR FROM Product Scopes. `productGroupID`
> - `constraintName`: ROLLUP FROM Constraints.`constraintName` GROUPED BY `constrainTypeID`
>Eliminate:
> - `ratings`
> - `design`
>Update:
> - `businessSegment`: MIRROR FROM Product Scopes.`productGroupID`

>[!note] Sem necessidade de Reports para esta tab

---

### Scopes

**ISO clause:** §4.3 (scope boundaries of the QMS)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `scopeID` | PK | |
| `scopeName` | string | e.g., Uprating, Temperature Reduction, Redesign |
| `scopeOpportunity` | enum: "lifetime Extension", "Increase Capability", "Dieletic Failure" - multivalued| Opportunity tags |
| `isActive` | bool | |


>[!note] Sem necessidade de Reports para esta tab
---

### Products

**ISO clause:** §8.1 (product and service provision)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `productID` | PK | |
| `productName` | string | |
| `isActive` | bool | |


>[!note] Sem necessidade de Reports para esta tab
---

### Product Class

**ISO clause:** §8.1 (product characteristics — technical specification basis)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `productClassID` | PK | Displayed as "Class Name" in UI |
| `voltageRate` | string | |
| `powerRating` | string | |


>[!note] Sem necessidade de Reports para esta tab
---

### Product Groups

**ISO clause:** §8.1 (commercial product grouping for planning)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `productGroupID` | PK | |
| `businessSegment` | enum: LPT/MT/DT | |
| `products` | rollup → Products (via: productGroupID) (display: productName, multivalued) | Products in this group |
| `productClassID` | rollup → Product Class (display: CONCAT(vontageRate,powerRating)) | |
| `isActive` | bool | |


>[!bug] Attributes
>Eliminate:
> -  `groupCode` 
> -  `groupName` 
>Update:
> -  `products` : single valued, not multivalued 
> -  `productClassID` : multivalued


>[!note] Sem necessidade de Reports para esta tab

---

## Module: Workload

### Tickets

**ISO clause:** §10.2 (nonconformity and corrective action — project-level issue tracking)

**Definition:** A Ticket is a project-linked work item that captures the execution context of a project's engineering process. It joins a Project, a Process, Products, Scopes, and a Forecast Scope into a single trackable record.

>[!tip] How tickets will be used 
>Customers, Planners e Managers terao acesso para criacao dos tickets para engeharia.
>Os tickets sao a porta de entrada para os jobs.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `ticketID` | PK | |
| `projectID` | FK → Projects (display: projectID) | |
| `customerName` | FK → Factories (display: factoryName) | Customer / requester factory |
| `processID` | FK → Processes (display: processName) | Process being executed for this ticket |
| `products` | rollup → Products via Payload (display: productName, multivalued) | Derived from the linked Process/Activity Payload |
| `scopes` | rollup → Scopes via Payload (display: scopeName, multivalued) | Derived from the linked Process/Activity Payload |
| `forecastScopeID` | FK → Forecast Scopes (display: scopeName) | Forecast Scope this ticket contributes to |
| `ticketOwner` | FK → People (display: userName) | Assigned owner |
| `ticketStatus` | enum: Open/InProgress/Resolved/Escalated/Closed | |
| `ticketCreatedAt` | datetime | |
| `ticketClosedAt` | datetime (nullable) | |
| `resolutionTime` | computed: ticketClosedAt − ticketCreatedAt (hours) | |
| `isEscalated` | bool | |
| `escalatedToEventID` | FK → Events (nullable) | |
| `jobs` | rollup → Jobs (via: ticketID) | All Jobs associated with this ticket |


>[!bug] Attributes
>Insert:
> - `targetDate`: datetime (when the ticket should be resolved)
> - `constraintName`: MIRROR → Forecast Scopes via `forecastScopeID`
> - `eventID`:  FK → Events (display: eventName) 
> - `taskID`: rollup -> Tasks via scopeID, productName, customerName
>Update:
> - `forecastScopeID`: rollup → Customers via customerName, eventID (display: CONCAT(scopeName,businessSegment,productClassID,productName))
> - `processID`: MIRROR → Forecast Scopes via `forecastScopeID`
> - `products`: MIRROR → Forecast Scopes via `forecastScopeID`
> - `scopes`: MIRROR → Forecast Scopes via `forecastScopeID`
> - `resolutionTime`: datetime (data de entrega prevista do ticket)
>Delete:
> - design:
> - `seBuilder` 
> - `ticketPriority` 

**Report-A — Tickets by Customer**
- `graph_type`: `bar`
- `rule`: Count of Tickets grouped by `customerName`
- `filters`: `["ticketStatus", "processID", "period", "priority"]`

>[!tip] Report-B
>- graph_type: pizza
>- rule: Count of tickets grouped by `scopeName`
>- filters: `["customerName", "period", "constraintName"]`

---

### Projects

**ISO clause:** §8.3 (design and development) + §8.4 (externally provided processes — customer scope)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `projectID` | PK | Displayed as project number, e.g. "0034" |
| `customerName` | FK → Factory (display: userName) | Customer name or factory |
| `products` | rollup → Products via Tickets (display: productName, multivalued) | Products linked through tickets |
| `projectOwner` | FK → People (display: userName) | |
| `projectStatus` | enum: In Progress/Planning/On Hold/Closed | |
| `ticketID` | rollup → Tickets (via: projectID) | All tickets belonging to this project |


>[!bug] Attributes
>Insert:
> - `clientName`: string (name of the final/external client)
> - `projectName`: string (name of the project)
> - `jobID`: MIRROR → Ticket via projectID
> - `estimatedTime`: soma dos `estimatedTime` das tarefas agrupadas por ticketID (consultar tabela Tickets via ticketID)
> - `executionTime`: soma dos `realExecutionTime` dos jobs agrupadas por ticketID (consultar tabela Jobs via ticketID)
>Update:
>Delete:

>[!tip] Report-A: Real vs Estimated Execution
>- graph_type:
>- rule: mostrar o tempo de execucao real (job) e estimado (tasks) para cada projeto.
>- filters: `["customerName","projectStatus"]`

---

### Jobs

**ISO clause:** §7.1.2 (people — execution-level resource assignment)

**Definition:** A Job is a concrete execution record that assigns a Role to a Ticket to perform a specific piece of work. It tracks the actual time spent (execution hours) and status for that assignment. Jobs are the primary source of actual usage data for the Control module.

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `jobID` | PK | |
| `jobName` | string | e.g., "Offer Design", "Mechanical Layout" |
| `ticketID` | FK → Tickets (display: ticketID) | Ticket this job belongs to |
| `roleID` | FK → Roles (display: roleName) | Role assigned to execute this job |
| `realExecutionTime` | decimal | Actual hours spent (usage recording) |
| `jobStatus` | enum: Queued/Active/Done/Stoped | |



>[!bug] Attributes
>Insert:
> - `taskID`:  rollup → Tasks via `ticketID` 
> - `startDate`: datetime (data de inicio prevista)
> - `endDate`: datetime (data final prevista)
> - `realEndDate`: datetime (data final executada)
> - `realStartDate`: datetime (data de inicio executada)
> - `projectName`: string (name of the project)
> - `predecesorJob`: rollup → Jobs via jobID (display: CONCAT(projectName, jobName))
> - `userID`: FK -> People (display: userName)
> - `customerName`: computed -> pega o customerName do projectID relacionado a ticketID desta tabela
> - `squadName`: computed -> nome do squad proveniente da tabela people relacionada ao userID definido nesta tabela
>Update:
> - `realExecutionTime`: computed -> realEndDate - realStartDate 
> - `roleID`: MIRROR de `userID`
>Delete:

>[!bug] Issue 
>A tabela de Jobs eh por onde sera feito o planejamento das atividades de engenharia. Sendo assim, nesta tabela eh preciso que o planejador seja capaz de: selecionar um `task` que servira de template para execucao do job; definir o inicio estimado; definir uma data de entrega; definir quem `peopleName` que executara o job, escolher um `job` de dependencia (para definir o sequenciamento de jobs), definir o tipo de dependencia (start-to -finish, finish-to-finish, etc), definir a data real de inicio, definir a data real de entrega, definir o status `jobStatus`.
>>[!note] People
>>A pessoa da tabela `People` que sera escolhida para executar o `job` deve ser previamente filtrada pelo `roleID` da `task` selecionada como template de execucao do `job`

**Report-A — Job Throughput**
- `graph_type`: `line`
- `rule`: Count of Jobs reaching `jobStatus = Done` plotted by week
- `filters`: `["roleID", "period"]`

**Report-B — Workload by Owner**
- `graph_type`: `bar`
- `rule`: SUM(`executionTime`) grouped by `roleID`
- `filters`: `["jobStatus", "ticketID", "period"]`

---

## Module: Control

>[!warning] Attribute List review
>Altere a lista de atributos de todas as tabelas do modulo de controle para que os reports que foram definidos possam ser aplicados.
>Lembrando que as tabelas do modulo de Control nao terao formularios com entrada de novos itens, sao apenas queries das tabelas ja existentes em outros modulos.

### Capacity

**ISO clause:** §7.1.2 (people resources) + §6.2 (planning — available capacity input)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `capacityID` | PK | |
| `departmentID` | FK → Departments (display: departmentName) | |
| `roleID` | FK → Roles (display: roleName) | |
| `periodType` | enum: Annual/Quarter/Month | |
| `periodYear` | int | |
| `periodQuarter` | int (nullable) | |
| `periodMonth` | int (nullable) | |
| `availableHours` | decimal | Total available hours for this role/department in period |
| `allocatedHours` | computed: SUM(Jobs.executionTime WHERE roleID + period match) | Hours already assigned via Jobs |
| `utilization` | computed: (allocatedHours / availableHours) × 100 | Displayed as % |
| `locationID` | FK → Locations (display: locationName) | |
| `factoryID` | FK → Factories (display: factoryName) | |


>[!bug] Attributes and Filters
>Update:
> - allocatedHours: `executionTime` das `tasks` relacionado aos forecastScopes de cada forecastID em um determinado periodo.
> - availableHours: total de horas disponiveis para os `rolesID` selecionado no periodo selecionado
> - periodStart: escolha do mes e ano de inicio da analise do report
> - periodFinish: escolha do mes e ano do fim da analise do report

**Report-A — Capacity vs. Allocation**
- `graph_type`: `bar`
- `rule`: `availableHours` vs. `allocatedHours` side by side grouped by `roleName`
- `filters`: `["periodStart", "eventTitle", "periodFinish", "factoryID", "roleID", "functionName"]`

>[!note] Report-A test
>datasets:
> - TABLE Tickets:
>   - ticketID: 001
>     - resolutionTime: 10-25-2026 (MM-DD-YYYY)
>     - eventName: "Offer Calculation Requested"
>     - taskID: 045 
>       - executionTime: 15  
>       - parentStepID: 033
>       - roleName: "SR Mechanical Designer"
>     - taskID: 032 
>       - executionTime: 8  
>       - parentStepID: 015
>       - roleName: "SR Mechanical Designer"
>     - taskID: 012
>       - executionTime: 5  
>       - parentStepID: 032
>       - roleName: "JR Electrical Designer"
>     - taskID: 033 
>       - executionTime: 8  
>       - parentStepID: 045
>       - roleName: "JR Mechanical Designer"
> - TABLE Forecasts:
>   - forecastID: 002
>     - periodStart: 09-2026 (mm-yyyy)
>     - periodFinish: 01-2027 (mm-yyyy)
>     - eventName: "Offer Calculation Requested"
>       - taskID: 045 
>         - executionTime: 15  
>         - roleName: "SR Mechanical Designer"
>       - taskID: 032 
>         - executionTime: 8  
>         - roleName: "SR Mechanical Designer"
>       - taskID: 012
>         - executionTime: 5  
>         - roleName: "JR Electrical Designer"
>       - taskID: 033 
>         - executionTime: 8  
>         - roleName: "JR Mechanical Designer"
>Query:
>   - utilizar o periodFinish inserido no report.
>     - WHILE Report.periodFinish >= Tickets.resolutionTime
>       - somar os executionTime da cadeia de tasks na tabela Tickets de acordo com os parentIDs.
>       - fazer um calculo retroativo da soma do passo anterior para chegar na data de inicio do ticket (periodStart)
>       - SE ticket.periodStart >= report.periodStart, incluir a somatorio de executionTime em allocatedHours
>       - SE NAO incluir em allocatedHours apenas a soma do tempo que se encontra dentro do periodo report.periodStart e report.periodFinish
>  - O executionTime proveniente da tabela de Forecasts serao alocados na variavel availableHours. Neste caso eh mais simples o calculo pois essa tabela ja tera o Forecast.periodStart e Forecast.periodFinish para ser comparado com report.periodStart e report.periodFinish, sendo apenas necessario somar e agrupar os dados conforme a rule do report A.

**Report-B — Utilization by Function**
- `graph_type`: `bar`
- `rule`: `utilization` % grouped by `functionName`
- `filters`: `["period", "factoryID", "roleID", "functionName"]`

---

### Usage

**ISO clause:** §9.1 (monitoring and measurement — resource consumption tracking)

>[!important] Reference Dataset
>The usage reports should reference the Jobs table for Role and Function usage

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `usageID` | PK | |
| `regionID` | FK → Regions (display: regionName) | |
| `departmentID` | FK → Departments (display: departmentName) | |
| `periodType` | enum: Annual/Quarter/Month | |
| `periodYear` | int | |
| `periodMonth` | int | |
| `usedHours` | decimal | Actual hours consumed (from Jobs.executionTime) |
| `plannedHours` | decimal | From Forecast Scopes estimatedHours |
| `variance` | computed: usedHours − plannedHours | Positive = over-plan, negative = under-plan |
| `reportedAt` | datetime | |
| `reportedBy` | FK → People (display: userName) | |

**Report-A — Usage Trend**
- `graph_type`: `line`
- `rule`: `usedHours` plotted by period, one series per `functionName`
- `filters`: `["customerName", "functionName", "period", "squadName"]`

**Report-B — Usage Heatmap**
- `graph_type`: `heatmap`
- `query`: mapa de calor das `roleName` mais utilizados por numero de jobs alocados
- `filters`: `["customerName", "functionName", "period", "squadName"]`

---

### Productivity

**ISO clause:** §9.1.1 (monitoring, measurement, analysis — efficiency KPIs)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `productivityID` | PK | |
| `teamID` | FK → Departments (display: departmentName) | Displayed as "Team" in the UI |
| `periodType` | enum: Annual/Quarter/Month | |
| `periodYear` | int | |
| `periodMonth` | int | |
| `output` | decimal | Actual deliverables or hours produced |
| `target` | decimal | Planned target for the period |
| `efficiency` | computed: (output / target) × 100 | Displayed as % |
| `factoryID` | FK → Factories (display: factoryName) | |

**Report-A — Productivity Index**
- `graph_type`: `donut`
- `rule`: Count of teams grouped by efficiency bucket (e.g., <80% / 80–100% / >100%)
- `filters`: `["funtionID", "factoryID", "period"]`

>[!tip] Report-C - Tarefas superdimensionadas
>- graph_type:
>- rule: quantidade de Tarefas que poderiam ser feitas por recursos menos experientes (`levelRank`)
>- filters: processName

>[!tip] Report-D - produtividade marginal 
>- graph_type:
>- rule: Quanto sera o ganho do processo ou evento escolhido ao acrescentar uma quantidade extra de um determinado `roleName`
>- filters: processName, eventName, roleNAme, roleExtraQuantity

---

## Module: Talent

### Squads

Criar uma nova tabela para squads.
Squads servirao para agrupar `people` de forma que o gestor possa simular forecastScopes por squads.

>[!tip] Attributes
> - `squadID`: Auto-generated
> - `squadName`: string
> - `squadType`: enum (outsource, internal)
> - `managerName`: string
> - `managerEmail`: string

>[!note] Sem necessidade de Reports para esta tab

### Roles

**ISO clause:** §5.3 (organisational roles, responsibilities, and authorities)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `roleID` | PK | |
| `roleName` | string | e.g., "Planner", "Design Engineer" |
| `functionID` | FK → Functions (display: functionName) | Functional area this role belongs to |
| `skillLevelID` | FK → Skill Levels (display: levelName) | Required proficiency level |
| `graduationID` | FK → Graduation (display: graduationName) | Required educational background |
| `quantity` | int | Number of headcount allocated to this role |
| `isActive` | bool | |
| `people` | rollup → People (via: roleID) | People currently holding this role |


>[!bug] Attributes
>Insert:
> - `overheadCost`: media dos `personalCost` dos recursos da tabela People via roleID 
> - `taskName`: rollup -> Tasks via roleID
>Delete:
> - `departmentID`

**Report-A — Roles by Function**
- `graph_type`: `donut`
- `rule`: Sum of `quantity` grouped by `functionID` (headcount distribution by function)
- `filters`: `["functionID", "skillLevelID", "isActive"]`

>[!tip] Report-B - Tasks by role
>- graph_type: pizza
>- rule: Count of tasks grouped by roleName with headCount > 0
>- filters: levelName

---

### Skill Levels

**ISO clause:** §7.2 (competence — proficiency definitions)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `skillLevelID` | PK | |
| `levelName` | string | e.g., Junior / Senior / Expert |
| `levelDescription` | text | e.g., "0–3 years of experience" |
| `levelRank` | int (1 to 5) | Ordering key (1 = lowest) |
| `roles` | rollup → Roles (via: skillLevelID) | |


**Report-A — Skill Level Mix**
- `graph_type`: `bar`
- `rule`: SUM(Roles.quantity) grouped by `levelName`
- `filters`: `["functionID"]`

---

### Functions

**ISO clause:** §7.2 (competence — functional scope definitions)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `functionID` | PK | |
| `functionName` | string | e.g., Electrical Design, Mechanical Design, Analyst |
| `roles` | rollup → Roles (via: functionID) (display: roleName, multivalued) | Roles that belong to this function |

**Report-A — Headcount by Team**
- `graph_type`: `bar`
- `rule`: SUM(Roles.quantity) grouped by `functionName`
- `filters`: `[]`

---

### Education

**ISO clause:** §7.2 (competence — education/qualification requirements)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `graduationID` | PK | |
| `graduationName` | string | e.g., Electrical Engineering, Mechanical Engineering |
| `field` | string | e.g., Engineering, Technical |
| `roles` | rollup → Roles (via: graduationID) | |

**Report-A — Graduation Fields**
- `graph_type`: `donut`
- `rule`: SUM(Roles.quantity) grouped by `field`
- `filters`: `[]`

---

### Competence

**ISO clause:** §7.2 (competence — mapping skills to roles, scopes, products)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `competenceID` | PK | |
| `roleID` | FK → Roles (display: roleName) | |
| `scopeID` | FK → Scopes (display: scopeName) | |
| `productID` | FK → Products (display: productName) | |
| `skillLevelID` | FK → Skill Levels (display: levelName) | Required proficiency |
| `isRequired` | bool | Whether this competence is mandatory |


>[!bug] Attributes
>Insert:
> - `taskID`: rollup -> Tasks via roleID (display: taskName)
> - actionID: MIRROR -> Tasks via taskID (display: actionName)
> - activityID: MIRROR -> Tasks via taskID (display: activityName)
> - constrainID: rollup -> Tasks via taskID (display: constraintName) multivalued
> - competenceName: computed (CONCAT(activityName,'-',actionName,'for',FORECAH`[scopeName]`,'of',FOREACH`[productName]`,'applied to',FOREACH`[{constrainTypeName: constraintName}]` ))
> - resources: list of all `channelName` of every `input` and `outputs` from Tasks via taskID
> - isCertified: computed -> Onboarding via competenceID
>Update:
> - scopeID: rollup -> Tasks via taskID (display: scopeName) multivalued
> - productID: rollup -> Tasks via taskID (display: productName) multivalued
>Delete:
> - `workflowID`
> - certifiedAt
> - certifiedBy

**Report-A — Competence Coverage Heatmap**
- `graph_type`: `heatmap`
- `rule`: Matrix of Role (rows) × Scope (columns); cell = % of required competences that are `isCertified`
- `filters`: `["scopeID", "productID", "roleID"]`

---

### People

**ISO clause:** §5.3 (responsible individuals) + §7.1.2 (people resources)

**Complete attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `userID` | PK | |
| `userName` | string | |
| `userEmail` | string | |
| `location` | FK → Factories (display: factoryName) | |
| `isActive` | bool | |
| `hireDate` | date (nullable) | |
| `functionID` | FK → Functions (display: functionName) | |


>[!bug] Attributes
>Insert:
> - `personalCost`: decimal 
> - `squadID`: FK -> Squads (display: squadName)
> - `onboardID`: computed -> Onboarding via userID

**Report-A — Headcount by Team**
- `graph_type`: `bar`
- `rule`: Count of active People grouped by `functionID`
- `filters`: `["departmentID", "locationID", "isActive"]`

---
### Onboarding

>[!tip] Attributes
> - userID: FK -> People (display: userName)
> - functionID: computed -> People via userID
> - roleID: rollup -> Roles via functionID (display: roleName)
> - competenceID: rollup -> Competence via roleID (display: competenceName)
> - isCertified: bool
> - scopeName: computed -> Competence via roleID
> - productName: computed -> Competence via roleID
> - resources: computed -> Competence via roleID
> - constraintName: computed -> Competence via roleID (display: FOREACH(`[{constrainTypeName: constraintName}]`))
> - certifications: string

---
## New Tables Required for Reporting


These entities exist in the EDQMS ER-UML (LucidChart page 1) but are absent from `datamodel.json`. They are needed to close the ISO 9001:2015 coverage gaps identified in `EDQMS-01_DataModel_DesignRationale.md`.

**Suggested placement:** add a new `Quality` module to `datamodel.json` containing: Risks, Sources, Source Categories, Requirements, actionApplication, Event Log.

---

### Risks

**ISO clause:** §6.1.1 (risks and opportunities — identification and assessment)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `riskID` | PK | |
| `riskTitle` | string | |
| `riskDescription` | text | |
| `riskCategory` | enum: Threat/Opportunity | |
| `riskSeverity` | int 1–5 | Impact rating |
| `riskLikelihood` | int 1–5 | Probability rating |
| `riskPriorityNumber` | computed: riskSeverity × riskLikelihood | Cochran RPN |
| `riskOwner` | FK → People (display: userName) | |
| `riskStatus` | enum: Open/UnderTreatment/Closed/Accepted | |
| `riskCreatedAt` | datetime | |
| `riskReviewedAt` | datetime (nullable) | Date of last RPN re-assessment |
| `eventID` | FK → Events (display: eventTitle) (nullable) | Triggering event |
| `requirementID` | FK → Requirements (display: requirementName) (nullable) | Associated interested-party requirement |
| `actions` | rollup → Actions (via: riskID) | Actions addressing this risk |

**Report-A — Risk Priority Matrix**
- `graph_type`: `scatter`
- `rule`: X-axis = `riskLikelihood`, Y-axis = `riskSeverity`, bubble size = `riskPriorityNumber`, colour = `riskCategory`; quadrant lines at 3/3
- `filters`: `["riskCategory", "riskStatus", "owner", "period"]`

**Report-B — Open Risk Register**
- `graph_type`: `table`
- `query`: Risks where `riskStatus` IN (Open, UnderTreatment); columns: title, category, severity, likelihood, RPN, owner, status, linked action count, last reviewed
- `filters`: `["riskCategory", "riskStatus", "owner"]`

---

### Sources

**ISO clause:** §4.1 (external and internal issues)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `sourceID` | PK | |
| `sourceName` | string | |
| `sourceCategoryID` | FK → Source Categories (display: sourceCategoryName) | |
| `sourceOwner` | FK → People (display: userName) | |
| `sourceDescription` | text | |
| `isActive` | bool | |
| `events` | rollup → Events (via: sourceID) | Events linked to this source |
| `requirements` | rollup → Requirements (via: sourceID) | Requirements that originate from this source |

**Report-A — Events by Source Category**
- `graph_type`: `bar`
- `rule`: Count of Events grouped by `sourceCategoryID`
- `filters`: `["sourceCategoryID", "period", "isActive"]`

**Report-B — Source → Event → Risk Traceability**
- `graph_type`: `table`
- `query`: Sources with event count, risk count, open risk count; traceable chain from source to event to risk
- `filters`: `["sourceCategoryID", "isActive"]`

---

### Source Categories

**ISO clause:** §4.1 (classification of issues — internal vs. external, customer, regulatory, etc.)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `sourceCategoryID` | PK | |
| `sourceCategoryName` | string | e.g., Customer, Regulatory, Internal |
| `sourceCategoryDescription` | text | |
| `sources` | rollup → Sources (via: sourceCategoryID) | |

*No dedicated dashboard report — used as a filter dimension in Sources and Events reports.*

---

### Requirements

**ISO clause:** §4.2 (understanding the needs and expectations of interested parties)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `requirementID` | PK | |
| `requirementName` | string | |
| `requirementDescription` | text | |
| `sourceID` | FK → Sources (display: sourceName) | Originating interested party |
| `requirementType` | enum: Customer/Statutory/Regulatory/Internal | |
| `isActive` | bool | |
| `productID` | FK → Products (display: productName) (nullable) | Product the requirement applies to |
| `risks` | rollup → Risks (via: requirementID) | Risks associated with this requirement |

**Report-A — Requirements by Type**
- `graph_type`: `donut`
- `rule`: Count of Requirements grouped by `requirementType`
- `filters`: `["sourceID", "isActive", "productID"]`

**Report-B — Requirement-to-Risk Compliance**
- `graph_type`: `table`
- `query`: Requirements joined with Risks; columns: requirement name, type, source, linked risk count, open risk count, highest RPN
- `filters`: `["requirementType", "sourceID", "isActive"]`

---

### actionApplication

**ISO clause:** §6.1.2(b) (classification of quality management actions)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `applicationID` | PK | |
| `applicationName` | enum: Risk Management/Control/Communication/Monitoring/Improvement | |
| `applicationDescription` | text | |
| `isoClause` | string | e.g., "6.1.2", "8", "7.4", "9.1", "10" |
| `actions` | rollup → Actions (via: applicationID) | |

*Lookup table — no dedicated dashboard report. Used as a filter dimension in Actions reports.*

---

### Event Log

**ISO clause:** §9.1.1 (monitoring) + §10.2 (nonconformity traceability — audit trail requirement)

**Attribute list:**

| Attribute | Type | Notes |
|---|---|---|
| `logID` | PK | |
| `eventID` | FK → Events (display: eventTitle) | |
| `previousStatus` | string | Status before change |
| `newStatus` | string | Status after change |
| `changedAt` | datetime | |
| `changedBy` | FK → People (display: userName) | |
| `changeNote` | text (nullable) | |

**Report-A — Event Resolution Time Distribution**
- `graph_type`: `bar`
- `rule`: Count of resolved Events grouped by resolution time buckets (<1h / 1–8h / 8–24h / 1–7d / >7d)
- `filters`: `["period", "owner", "priority"]`

**Report-B — Event Audit Trail**
- `graph_type`: `table`
- `query`: Full state-change history for a selected event; columns: previous status, new status, changed by, changed at, note
- `filters`: `["eventID", "changedBy", "period"]`

---

## Entities Intentionally Excluded from Dedicated Reports

The following entities function as **lookup/reference tables** or **junction tables**. They appear as filter dimensions, FK targets, or rollup sources in the reports above but do not warrant their own dashboard widget:

| Entity | Reason |
|---|---|
| Source Categories | Lookup; used as filter in Sources and Events reports |
| Scope Categories | Lookup; used as filter in Scopes report |
| Constraint Types | Lookup; used as filter in Constraints report |
| actionApplication | Lookup; used as filter in Actions report |
| Process Boundary | Metadata on Processes; reported through Processes |
| Payload | Association class; surfaced through Tasks (products/scopes columns) |
| Procedure | Knowledge documentation; surfaced as coverage flag in Activities report |
| Operation | Steps within Procedure; too granular for a standalone dashboard widget |
| Property | Resource tag on Operations; too granular |
| Interface | Sub-entity of Channel; reported through Channels |
| Tool | Resource entity; can be a detail column in Activities |
| Region / Location / Business Unit / Department | Org-structure lookups; used as filters throughout |
| Specs | Product technical specs; surfaced as columns in Product Scopes (ratings) |
