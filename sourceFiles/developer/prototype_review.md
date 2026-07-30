# Como usar esta instrucao

- [ ] verificar #datamodel para indentificar o que foi alterado em relacao a versao usada no wireframe.
- [ ] este documento sera utilizado como prompt para code review e planejamento de issues

## Documentos de referencia

o simbolo `#` sera utilizado para identificar as referencias abaixo sempre que forem indicadas neste documento.

`wireframe` = ./prototype_wireframe/Global Engineering Portal (standalone).html
`datamodel` = ../../prototype/data/datamodel.json
`design-system` = ./prototype_designSystem.html

# Revisoes de interface

Todas as referencias de blocos e interfaces do shadcn devem ser aplicadas atraves do #design-system especifico deste projeto

## Dashboard

Use a inverface de dahsboard 01 do shadcn (npx shadcn@latest add dashboard-01) como padrao para todas as telas (tabs)
Para identificar se havera `cards` ou `reports` na tela, verifique #datamodel

## Login
- [ ] criar uma tela de login
- [ ] usar npx shadcn@latest add login-01 como bloco de interface.
- [ ] login deve ser apenas `username` e `password`
  - [ ] username == se-admin
  - [ ] password == @SiemensEnergy2026

## Settings

- [ ] Deixar toda a plataforma em darkmode por padrao.
  >[!note] gh-task review/plan
  >Nao eh necessario criar um botao de toggle entre dark e lighmode para o prototipo, mas eh importante criar uma issue para que isto seja feito no future
  >O cadastro de calendarios pode ser feito em uma proxima atualizacao, no protipo vamos considerar que os recursos trabalham de segunda a sexta feira 7 horas por dia para efeito de calculo de relatorios

- [ ] Criar um configurador de calendarios.
  - [ ] Criar templates de calendario
    - [ ] definir dias uteis da semana
    - [ ] definir horas uteis do dia util
    - [ ] definir feriados e folgas no calendario
  >[!note] gh-task review/plan
  >O cadastro de calendarios pode ser feito em uma proxima atualizacao, no protipo vamos considerar que os recursos trabalham de segunda a sexta feira 7 horas por dia para efeito de calculo de relatorios

## Tabelas

- [ ] Utilizar o componente shadcn <DataTable>
- [ ] Summation Row: add a row in the end of every table to SUM all numerical attributes.
- [ ] As tabelas devem possuir o mesmo componente da dashboard0-01 do shadcn, mesmo estilo de paginacao, rows per pager, etc.
- [ ] Controles: os controles sao botoes que ficam no topo da tabela que mudam o comportamento da tabela e seus itens
  - [ ] Edit: Quando apenas um item estiver selecionado na tabela, habilitar este botao
  - [ ] Delete: Se um ou mais itens estiverem selecionados na tabela, habilitar este botao
  - [ ] Customize Columns: conforme #wireframe
  - [ ] Filters: conforme table-filters e #wireframe
  - [ ] New Item: conforme #wireframe e drawers.

## Cards

```json
  "cards": [
    {
      "Card 1-1": /*ordem em que o card deve aparecer na tela. Os numeros representam (linha - coluna) do grid*/ {
        "title": "Title of the card to be displayed above the main-data",
        "card-rules": {
          "main-data": "Dado em destaque no card",
          "trend-data": "comportamento do dado, se estiver em ascensao deve possuir uma seta pra cima com os dados em verde, caso controrio, deve possuir uma seta pra baixo e com os numeros em vermelho. Posicionar a trend a frente do main-data no card",
          "detail-data": "deve ficar abaixo do main-data em fonte reduzida, apresentando detalhes sobre o main-data"
        }
        "card-component": "UI component reference",
        "card-tooltip": "explicacao sobre o que o card representa"
      }
    }
```

## Drawers

- [ ] Sempre que um formulario {datamodel.table.form.field-name:type=="multi-selection" || "selection" || "search"} possuir um campo de selecao de itens relacionados a outra tabela, adicionar um botao de "incluir novo 'field-name'" que devera abrir uma nova aba de drawer. O #wireframe ja possui esse tipo de funcionalidade.

### Forms

field-type: este parametro eh composto de uma objeto com uma Key e um Value. A key representa o type do componente, e o value representa o source.
Exemplo 1: {"month": "html"}
  - month:
    ```HTML
    <HTML>
      <input type=month />
    </HTML>
    ```

Exemplo 2: {"Textarea": "shadcn-field"}
  - Feedback
    ```HTML
    import {
      Field,
      FieldDescription,
      FieldGroup,
      FieldLabel,
      FieldSet,
    }
    from "@/components/ui/field"
    import { Textarea } from "@/components/ui/textarea"

    export function FieldTextarea() {
      return (
        <FieldSet className="w-full max-w-xs">
          <FieldGroup>
            <Field>
              <FieldLabel htmlFor="feedback">Feedback</FieldLabel>
              <Textarea
                id="feedback"
                placeholder="Your feedback helps us improve..."
                rows={4}
              />
              <FieldDescription>
                Share your thoughts about our service.
              </FieldDescription>
            </Field>
          </FieldGroup>
        </FieldSet>
      )
    }

    ```

Exemplo 3: {"Combobox": "shadcn-combobox"}
  - Combobox
    ```HTML
    import {
      Combobox,
      ComboboxContent,
      ComboboxEmpty,
      ComboboxInput,
      ComboboxItem,
      ComboboxList,
    } from "@/components/ui/combobox"
    const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

    export function ExampleCombobox() {
      return (
        <Combobox items={frameworks}>
          <ComboboxInput placeholder="Select a framework" />
          <ComboboxContent>
            <ComboboxEmpty>No items found.</ComboboxEmpty>
            <ComboboxList>
              {(item) => (
                <ComboboxItem key={item} value={item}>
                  {item}
                </ComboboxItem>
              )}
            </ComboboxList>
          </ComboboxContent>
        </Combobox>
      )
    }
    ```

Schema on #datamodel
```json
{
  "form": {
    "steps": {
      "step-title": {
        "step-description": "string",
        "step-order": "integer", /* vertical position of the step in the form */
      }
    }
    "fields": {
      "field-name": {
        "field-type": [{text: html}, {month: html}, {range-picker: shadcn}],
        "tooltip": "insert a description on the UI element",
        "step": "step-title",
        "check": "appears only if the value of a given field, or field combination, matches a criteria",
        "field-rule": "a rule on how to display the items of the field or the input constraints."
      }
    }
  }
}
```

Example: Jobs Table form
```json
{
  "form": {
    "steps": {
      "SELECT TEMPLATE": {
        "step-description": "Select a task to create baselines and filter roles",
        "step-order": 1,
      }
      "SCHEDULE": {
        "step-description": "Select when the task must be delivered",
        "step-order": 2,
      }
    }
    "fields": {
      "Ticket": {
        "field-type": {"select": "shadcn"},
        "tooltip": " ",
        "step": "SELECT TEMPLATE",
        "check": null,
        "field-rule": null
      }
      "Task Template": {
        "field-type": {"Groups": "shadcn-combobox"},
        "tooltip": " ",
        "step": "SELECT TEMPLATE",
        "check": "disable field until field Ticket has been selected",
        "field-rule": "rollup -> field.Ticket.input (via: Tickets Form) -> Tickets(processID) -> Tasks (via: processID); display: taskName FILTER BY scopeID (via: ticketID -> productScopeID -> scopeID) GROUP BY processName"
      }
      "Planned Execution Period": {
        "field-type": {"Range Picker": "shadcn-Date Picker"},
        "tooltip": " ",
        "step": "SCHEDULE",
        "check": "disable field until Ticket and Task Template inputes has been selected",
        "field-rule": null
      }
    }
  }
}
```

### Report-Filters

- [ ] os filtros serao definidos da mesma forma que os forms, com a mesma estrutura, ou seja: teremos um botao em cada filtro que abrira um drawer a direita e nele estarao os inputs

  >[!note] gh-task review/plan
  >Faca uma analise sobre a melhor forma de indicar os filtros dos relatorios. caso encontre uma alternativa que melhore a experiencia do usuario, sinta-se a vontade em aplica-la ao inves do modelo sugerido acima de botao e drawer

- [ ] O botao de "reset" deve ficar dentro do drawer.
- [ ] Cada report <div> deve ter seu proprio botao de filtro

### Table-Filters

- [ ] Os filtros de tabelas devem ser feitos da mesma forma que o #wireframe.
- [ ] Os filtros das tabelas devem seguir o padrao do #wireframe, um botao que abre um drawer a direita.
  - os botoes de filtro de tabela serao habilitados ou nao a depender do valor do parametro `table-filters` em #datamodel

## Sidebar

- [ ] aplicar sidebar 07 (npx shadcn@latest add sidebar-07)
  - [ ] Eliminar a estrutura de Tabs das dashboards atuais para poder adotar a sidebar indicada. As tabs passam a integrar o menu dos modulos na sidebar

## Reports

- [ ] Nos reports onde nao foram indicados referencias do shadcn dentro do #datamodel, sinta-se livre para escolher uma referencia na biblioteca do shadcn que melhor represente as regras e filtros do relatorio.

>[!note] gh-task review/plan
>Crie testes para garantir que as tabelas e queries estao corretas para atender todos os relatorios cards

## Tabs (Dashboards)

- [ ] usar shadcn dashboard-01 (npx shadcn@latest add dashboard-01)  respeitando o componente de sidebar indicado neste documento
- [ ] Seguir o padrao de botoes de `Edit` `Delete` and `Customize Columns` conforme #wireframe
  - [ ] O botao de edit deve ser ativado quando apenas um item da tabela estiver selecionado
  - [ ] O botao de delete deve ser ativado quando um ou mais itens forem selecionados na tabela
- [ ] a quantidade de cards e reports de uma dashboard sera definida em #datamodel

## Tabela de subitens

- [ ] As tabelas de subitens podem apresentar agrupamentos de mais de uma tabela. Vide a tabela atual da dashboard `Events` no prototipo como exemplo destes agrupamentos (grupo 1: Tasks; Grupo 2: Tickets)
  - a lista de tabelas que deve ser renderizadas como subitens sao definidos em `subitem-tables` in the #datamodel

  ```json
    "subitem-tables": [
      "Tasks",
      "Tickets"
    ]
  ```

- [ ] As tabelas de subitens tambem podem possuir uma tabela de subitem. Esse comportamento `nested` das tabelas de subitem eh identificado em #datamodel da seguinte forma:
  ```json
    "subitem-tables": [
      "Product Scopes -> Competence"
    ]
  ```
  - Neste caso a tabela de subitem Product scope possui uma tabela nested de subitem para Competence

---

# Modulos


## quality

- [ ] Elimine este modo completamente. Fara parte de uma futura release


## Control

### Capacity

- [ ] Adicionar um botao na interface do relatorio A para filtrar os forecasts desconsiderando todos os dados de forecasts do tipo Draft. Pode ser um radiobutton

## Overview

- [ ] A tabela de overview sera um compilado de cards e dados existentes dentro das dashboard (tables) de cada modulo.
- [ ] Os cards e relatorios a serem adicionados em Overview serao determinados pelo parametro `overview-dislay` em cada card ou report dentro de #datamodel
- [ ] Todos os cards e graficos (reports) dentro da dashboard de overview devem possuir um botao (details) com o link da dashboard de referencia.
- [ ] todos os filtros dos graficos (reports) devem ser desabilitados para a dashboard de Overview. Por isso temos o botao `details` para levar para a dashboard de origem dos relatorios, para que o usuario possa aplicar filtros e analisar melhor os dados.

## Customers


### Factories

- [ ] Inserir relatorios conforme indicado no #datamodel

#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Factories por os dados abaixo sem a necessidade de inserir mais nenhuma linha nesta tabela para que sejam realizados os testes


| Name | City | Country | Segment | Region |
| --- | --- | --- | --- | --- |
| PN | Nuremberg | Germany | LPT | EMEA |
| TUSA | Jundiai | Brazil | LPT | Americas |
| STW | Weiz | Austria | LPT | EMEA |
| KPT | Zagreb | Croatia | LPT | EMEA |
| STGZ | Guangzhou | China | LPT | APAC |
| STDD | Dressden | Germany | MPT | EMEA |
| STL | Linz | Ausria | MPT | EMEA |
| STN | Trento | Italy | MPT | EMEA |
| STCK | Jinan | China | MPT | APAC |
| STWH | Wuhan | China | MPT | APAC |
| STM | Guanajuato | Mexico | MPT | Americas |
| DB | Budapeste | Hungary | DT | EMEA |
| DK | Kirchhelm | Germany | DT | EMEA |
| TN | Nuremberg | Germany | DT | EMEA |
| JXN | Jackson | USA | DT | Americas |
| SAT | Trenjo | Colombia | DT | Americas |
| STCA | Trois-Riviere | Canada | DT | Americas |


### Forecasts

- [ ] Inserir tabela de subitens conforme indicado em #datamodel
- [ ] eliminar os relatorios para esta dashboard
- [ ] atualizar atributos conforme #datamodel
- [ ] report:
  - [ ] inserir um report para mostrar o monthly rate entre horas budgetadas de acordo com os forecast (usageQuota) VS estimatedHours dos Tickets

### Forecast Scopes

- [ ] atributos
  - adicionado `quantity` para calcular o tempo estimado dos forecasts

## Operation

- [ ] atualizar dashboards conforme revisoes do #datamodel

### Events


#### Mockup Data

- [ ] usar os dados salvos em ./events.csv como mockup para a tabela de Events

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Events por os dados de ./events.csv
>Voce pode criar dados adicionais para esta tabela.
>Use esta tabela como referencia contextual pra criar os mockups de outras tabelas relacionadas.


### Process

- [ ] tabela de subitens:
  - [ ] workflows (ordenado por identationID)-> nested with Tasks

#### Mockup Data

>[!warning] Review existent mockup data
>Inclua este item na tabela mockup de Process
>Voce deve criar dados adicionais para esta tabela.


| ID | Event | Name | Description | Registry ID |
|---|---|---|---|---|
|PC01| Offer Calculation Request | Offer Electrical Design |   | ZXPTO0001-T |


### Activities

#### Mockup Data

>[!warning] Review existent mockup data
>Inclua os items abaixo na tabela mockup de Activities
>Voce deve criar dados adicionais para a tabela de mockup baseado no contexto gerado pelo exemplo abaixo


| ID | Activity |
|---|---|
| ACT01 |  Allocation |
| ACt02 |  Technical Assessment |
| ACT03 |  Technical Clarification |
| ACT04 | Data Collection|
| ACT05 | Offer Design|
| ACT06 | Operational Clarification|
| ACT07 | Technical Spectification|


### Actions


#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os itens da tabela mockup de Actions pelos intens abaixo 
>Voce NAO deve criar dados adicionais para esta tabela de mockup


| Name | Description |
| --- | --- |
| Approval | Go or No-Go decision about wheter an acitivity should move into the workflow |
| Assignment |Action of planing who should execute an activity |
|Check |Revise the execution of a given activity|
|Execution |Developing a given activity|
|Followup |Check activity status to update a plan|
|Registration |Insert a given activity on an inventory following certain rules|
|Release |Input the data generated during the execution of a given activity into a system|



### Workflows

- [ ] Atributos
  - identationID: descreve a relacao entre as atividades.
    - exemplo 1: um item com identationID de 2.1 tem a relacao `finish-to-finish` com o item 2
    - exemplo 2: um item com identationID de 2 tem a relacao `start-to-finish` com o item 1
    - exemplo 3: um item com identationID de 2-1 tem a relacao `start-to-start` com o item 2

#### Mockup Data

>[!warning] Review existent mockup data
>Inclua os items abaixo na tabela mockup de Workflows
>Voce deve criar dados adicionais para a tabela de mockup baseado no contexto gerado pelo exemplo abaixo


| ID | Process | Activity | Parent Step | Identation |
|---|---|---|---|---|
| WF01 | Offer Electrical Design | Allocation |  | 1 |
| WF02 | Offer Electrical Design | Technical Assessment |WF01| 2 |
| WF03 | Offer Electrical Design | Technical Clarification |WF02| 2.1 |
| WF04 | Offer Electrical Design |Data Collection|WF02| 2.2 |
| WF05 | Offer Electrical Design |Offer Design|WF02| 3 |
| WF06 | Offer Electrical Design |Operational Clarification|WF05| 3.1 |
| WF07 | Offer Electrical Design |Technical Spectification|WF05| 4 |



## Inventory


### Product scopes

- [ ] atributos
  - constraintID (FK -> Constraints; display: constraintName)

### Scopes


#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Scopes por os dados abaixo sem a necessidade de inserir mais nenhuma linha nesta tabela para que sejam realizados os testes

| Code | Name | Opportunity |
| --- | --- | --- |
| A.1 | Temperature Reduction |Lifetime Extension |
| A.2 | Uprating | Increase Capability |
| A.3 | Uprating with Windings Replacement| Increase Capability |
| A.4 | Repair with Windings Replacement | Dieletric Failure |
| B |Reduction of the volume of gases and moisture in the insulating oil​ |Lifetime Extension |
| C |Renewal of the paper/oil insulation system​|Lifetime Extension |
| D |Protection devices, wiring/cabling, cubicles, monitoring​|Lifetime Extension |
| E |Renovation of External Parts|Lifetime Extension |
| F |Replacement of bushings, shields/electrodes and CT's​|Lifetime Extension |
| G |Electrical and/or materials testing, inspection, evaluation and diagnosis​|Lifetime Extension |


### Products

#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Scopes por os dados abaixo sem a necessidade de inserir mais nenhuma linha nesta tabela para que sejam realizados os testes

| ID | Name |
| --- | --- |
| P01 | LPT |
| P02 | Autotransformer |
| P03 | Phase Shifter |
| P04 | HVDC |
| P05 | Reactors |
| P06 | MPT |
| P07 | IND |
| P08 | LDT |
| P08 | CRT |
| P09 | LIDT |
| P10 | TRAC |
| P11 | VR |
| P12 | CP |
| P13 | RENEW |


### Product Groups

#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Scopes por os dados abaixo sem a necessidade de inserir mais nenhuma linha nesta tabela para que sejam realizados os testes


| ID | Product | Segment | Class |
| --- | --- |--- |--- |
| P01 | LPT | LPT | CLS03, CLS04 |
| P02 | Autotransformer |LPT |  CLS03, CLS04 |
| P03 | Phase Shifter |LPT |  CLS07 |
| P04 | HVDC | LPT| CLS08 |
| P05 | Reactors |LPT | CLS06 |
| P06 | MPT |MPT | CLS01, CLS02|
| P07 | IND |MPT | CLS05 |
| P08 | LDT |MPT | CLS01, CLS02 |
| P08 | CRT | DT | CLS09 |
| P09 | LIDT |DT | CLS12, CLS13|
| P10 | TRAC |DT |CLS14 |
| P11 | VR |DT | CLS10 |
| P12 | CP |DT |CLS09 |
| P13 | RENEW | DT| CLS01, CLS12, CLS13 |


### Product Class

#### Mockup Data

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Scopes por os dados abaixo sem a necessidade de inserir mais nenhuma linha nesta tabela para que sejam realizados os testes


| ID | Voltage Rating | Power Rating |
| --- | --- |--- |
| CLS01 | <=145 | <=100 |
| CLS02 | <=300 | <=250 |
| CLS03 | <=550 | <=400 |
| CLS04 | >550 | >400 |
| CLS05 | ALL | ALL |
| CLS06 | ALL | ALL |
| CLS07 | ALL | ALL |
| CLS08 | ALL | ALL |
| CLS09 | ALL | ALL |
| CLS10 | ALL | ALL |
| CLS11 | ALL | ALL |
| CLS12 | <=36 | <=10 |
| CLS13 | <=72,5 | <=30 |
| CLS14 | ALL | ALL |
| CLS15 | ALL | ALL |


## Workload


### Tickets

- [ ] Atributos
  - ticketID
  - customerName
  - projectID
  - ticketDescription
  - eventID (display: eventName)
  - productScopeID (display: productScopeName)
  - ticketStatus (InProgress, Open, Resolved, Closed, Escalated)
  - ticketDueDate
  - taskId (rollup -> Tasks via: ticketID -> eventID -> productScopeID.scopeID -> productScopeID.productGroupID)
  - ticketExecutionTime (via: rollup.taskID.executionTime)

- [ ] Subitem table
  - Jobs (display: status = Active, Queued)

#### Mockup Data

- [ ] usar os dados salvos em ./tickets.csv como mockup para a tabela de Tickets

>[!warning] Review existent mockup data
>Substitua os dados de mockup da tabela Tickets por os dados de ./tickets.csv.
>Substitua os dados da coluna "Forecast Scope" do .csv com os dados de mockup da tabela Forecast Scope.
>Voce pode criar dados adicionais para esta tabela.
>Use esta tabela como referencia contextual pra criar os mockups de outras tabelas relacionadas.




