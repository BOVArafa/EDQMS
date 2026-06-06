--- 
content-type: context
subject: 
  - prototype
--- 

> Standard Operating Procedures address this gap by converting operational events into structured, traceable decision flows. The prototype aims to **validate and optimize** a template that ensures clarity, navigability, and auditability

Como neste momento a intencao do prototipo eh formatar um template (modelo de dados minimo) para criacao e gestao de procedimentos, nao precisamos de uma lista completa dos eventos que iniciam os processos de engenharia, basta selecionar alguns poucos de forma estrategica.


## Estrategia para selecao da fronteira do projeto
Ate este ponto, existe apenas uma fronteira mapeada. Por essa razao, eh a unica que pode ser selecionada para ser audidatada.
Essa fronteira tem como objetivo desenvolver o calculo de ofertas e propostas para os clientes da siemens Energy.
Fronteira recebe o nome de `Offer Process`

Os eventos que compoe essa fronteira sao:

| ID | Event | Description |
|:---| :--- | :--- |
|EVT001| Opportunity Development Request | Sales create the opprtunity and notifies the offer manager |
|EVT002| Offer Calculation Requested | Engineering receives a demand for creating an offer calculation |
|EVT003|FIA Support Requested|Finding investigation Analysis requested by the sales or offer manager|
|EVT004|FIA Report Released|Findings investigation Analysis Report is released |
|EVT005|Technical Data Requested|Engineering needs more information about the scope to be able to develop the offer calculation| 
|EVT006|Technical Data Released| Costumer or/and Local Engineering releases the documentation requested | 
|EVT008| Offer Calculation Released| Engineering releases the documentation necessary for the offer team to finish the proposal | 
|EVT009| Offer Calculation Revision Requested|Sales or the offer manager asks engineering to modify the offer calculation| 
|EVT010| Offer Rejected|The Final Offer is rejected by the customer| 
|EVT011|Offer Approved|The Final Offer is approved by the customer| 
|EVT012|Inspection Scope Requested|For complex repairs engineering may be asked to develop an inspection scope| 
|EVT013|Inspection Scope Released|Inspections as well as tests necessaries to develop technical scope, project and studies| 
|EVT014|Inspection Report Released|Field Service engineering develop report accordingly with the scope| 



## Validation Path decision
Existem dois caminhos para auditar os eventos escolhidos para a fronteira de processo definida:

### Track A: Project‑Oriented
This approach is a practical mapping based on real projects—either currently in development or already delivered. In this case, the outputs of each activity and the steps required to produce them are already defined; the effort focuses on documenting and mapping them.
- Pros
  Less time‑consuming to map procedure steps
  Based on real, validated project data
- Cons
  Requires a large number of projects to fully cover all activity procedures across different service scopes and product types

### Track B: Service Scope‑Oriented
This approach is a hypothetical mapping based on service scopes. The activity procedures, steps, and outputs are defined conceptually and designed rather than derived from completed projects.
- Pros
  Enables selection of the most contextually relevant service scopes
  Allows focusing on procedures with immediate operational impact
- Cons
  More time‑consuming, as procedure steps and activity outputs must be defined from scratch

O caminho escolhido para auditar 
