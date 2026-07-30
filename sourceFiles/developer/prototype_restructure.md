# Objetivo  

Apos uma mudanca organizacional na Siemens-Energy, que eh o cliente deste projeto, foi solicitado que o portal pudesse absorver diferentes times de design dentro da organizacao.
O atual prototipo levava em consideracao a operacao de uma engenharia de reparos de transformadores de potencia, mas esse departamento sera integrado a outros (como a engenharia de switch gear), o que demanda uma resstruturacao em alguns modulos para que o sistema possa ser utilizado por qualquer outro departamento de engenharia.

>[!note] Claude-Code Assessment 
>Voce deve levar o objetivo em conta sempre que for fazer seu code review.
>Voce pode sugerir novas features ou novo relacionamento das entidades do modelo de dados
>para que o prototipo atenda aos novos objetivos.


# Mudancas no modelo de dados

## Constraints

Essa dashboard deve ser renomeada para `Requirements` e transferida para o modulo `Portfolio`
Atualizar o datamodel.json para substituir os nomes de atributos e parametros de `constraint` ou `constrain` para `requirement`

Adicionar atributos:
- Scope: scopeID (display: scopeName)
- Product Group: productGroupID (display: CONCAT(productName + SPECS))

Alterar atributos:
- requirementTypeID (former `constrainTypeID`): FK -> Requirement Type (display: requirementTypeName)

### Requirement Type
apply `dashboard-order` = 0

Criar uma nova entidade chamada `Requirement Type` para cadastros dos tipos de requirements a serem selecionados na criacao de uma nova requirement.

Adicionar atributos:
- requirementTypeID: auto-generated
- requirementTypeName: VARCHAR
- requirementTypeDescription: TEXT

## Product Scopes 

Alterar atributos:
- requirementID (former constrainID): rollup (via: productGroupID + scopeID) (display: requirementName)
  - neste novo modelo os requirements serao definidos apos a selecao do scope e do product group. Ou seja, ao selecionar esses dois parametros, eh preciso fazer um rollup na tabela de requirements para filtrar aqueles vinculados ao scope e product group selecionados.

Alterar form:
- eleminar input `Constraints`


## Tasks

Por conta das mudancas no modelo das entidades do modulo `Portfolio`, nao sera mais necessario selecionar o `productScopeID` no cadastro das tarefas. Vide as regas em ##Competence e ##Jobs para entender melhor

Alterar attribute:
- customerName: FK -> Factories via: factoryName 
- requirementName (former constrainName): computed: taskID → Competence.requirementID (display: requirementName)
- functionID: computed: taskID → Competence.functionID (display: functionName)


Alterar Form:
- eliminar input: `Constraints`, `Function`, `Product Scope`
- adicionar input para `Customer` (attribute: `factoryName`)

## Competence

Corrigir os atributos dessa tabela e das tabelas relacionadas para reflitir os inputs de formulario abaixo

Form:
- selecionar functionName
- selecionar skillLevelTitle
- selecionar roleName (filtrado por skillLevelTitle + functionName )
- Selecionar scopeName
- Selecionar productGroupID
- Selecionar requirementName (filtrado por scopeName e productGroupID): multivalued
- selecionar eventName
- selecionar processName
- selecionar taskName (rollup -> Tasks via: eventName + processName )
- selecionar levelRank


## Jobs 

Corrigir os atributos dessa tabela e das tabelas relacionadas para reflitir os inputs de formulario abaixo

Form:
- Project: Fk -> Projects (display: projectName grouped by client)
- Ticket: rollup -> Tickets via: projectID (display ticketID grouped by customerName (factoryName))
- Task: rollup -> Tasks via: Ticket.processID + Ticket.customerName (display: taskName)
- Responsible: rollup -> Onboarding via: Ticket.scopeID + Ticket.productGroupID + Ticket.requirementID + taskName(via jobs input) + Onboarding.isCertified(true)
- Delivery Date: datetime input 
- Status: enum(Queued, Active, Done, Stoped)
- Real Start Date: ELIMINAR ESTE INPUT do formulario
- Real Finish Date: ELIMINAR ESTE INPUT do formulario

Adicionar attribute:
- jobBufferExecution: starts counting time every time a job status changes to Stoped

Alterar atributos;
- realStartDate: deve ser alterado quando o status do job alterar de Queued para Active
- realEndDate: deve ser alterado quando o status do job alterar de Active para Done
- realExecutionTime: computed: (realEndDate − realStartDate) - jobBufferExecution (DECIMAL)

