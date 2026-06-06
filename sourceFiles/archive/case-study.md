--- 
content-type: context
subject: 
  - project
  - method
--- 

# Purpose

Usar um caso real para validar o metodo de criacao de procedimentos tem algumas vantagens:

- Ao mapear os procedimentos de um caso real para uma determinada [fronteira](../sourceFiles/process_boundary.md), podemos garantir que o escopo de trabalho relacionado a este projeto pode ser replicado e desenvolvido pela engenharia. Isso significa que um cliente (unidade de negocio) ja pode solicitar a execucao de projetos com a mesmas caracteristicas para o hub global

- Domain experts trabalham melhor usando referencias reais ao inves de tentar imaginar a aplicacao de metodologias em casos abstratos

# Planning

Antes de se iniciar o estudo de caso (end-to-end) eh preciso definir os eventos que serao auditados para mensurar quanto tempo levara a fase de validacao.
Os eventos a serem escolhidos nao esta diretamente legados ao projeto ou escopo de servico, mais detalhes sobre a escolha dos processos estao no [planejamento do prototipo](../sourceFiles/prototype_plan.md)

# Case Selection

`Livorno` foi o projeto selecionado para o end-to-end validation.

Este projeto possui um escopo complexo o suficiente para mapear diversas interfaces para diferentes eventos, o que nos garante oportunidades de testar o modelo de dados e templates de criacao de procedimentos de forma mais abrangente.

## interfaces

As interfaces (interface entity in the data model) mapeadas para este projeto sao:

| ID | Owner | Business Unit | Department |
| :--- | :---| :---| :---|
| ITF-001 | Thomas | Nuremberg | Engineering|
| ITF-002 | Joao | Charlotte | Engineering|
| ITF-003 | Bicca | Linz | Engineering|
| ITF-004 | - | Weiz | Engineering|
| ITF-005 | - | Charlotte | Project Management|
| ITF-006 | - | Linz | Project Management|


## End-to-End Validation

Embora a intencao da [auditoria](../sourceFiles/event-audit.md)  nao seja o conteudo ou a abrangencia dos procedimentos, apenas a validacao do template para construi los, eh importante levar em conta o fato de que os stakeholders precisam ter material suficiente para entender qual sera o impacto da adocao deste prototipo no dia a dia da operacao.

Por essa razao precisamos selecionar os eventos que possibilitem essa maior comprrensao por parte dos stakeholders.
Abaixo a tabela com os eventos selecionados para este fim, indicando as interfaces produtoras e consumidoras (de acordo com o escopo do caso real selecionado) assim como o tempo estimado para desenvolvimento da auditoria de cada processo.

| Event | Producer | Consumer | Audit (hours) |
| :--- | :--- | :--- | :--- |
| Offer Calculation Requested | ITF-005 | ITF-002, ITF-003 | 18 |
|FIA Support Requested| ITF-005 |ITF-002, ITF-003 | 28 |
|Technical Data Requested| Linz, Charlotte | Nuremberg | 21 |
|Technical Data Released| Nuremberg | Linz, Charlotte | 12 |
| Offer Calculation Released| Charlotte, Linz | Linz, Charlotte,  | 18|

