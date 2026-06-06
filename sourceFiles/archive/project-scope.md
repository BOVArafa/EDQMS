---
content-type: context
subject: 
  - overview
  - project
---

# Siemens Energy Power Transformer Global Repair Hub

Em janeiro de 2026, a simenns energy entrou em contato comigo para auxilia-los em um projeto de implementacao de um hub de engenharia global para projeto de reparos de transformadores de potencia.
Foi solicitado que eu fiezesse uma [proposta](./PRP-C-0016.md) de consultoria para mapear os gaps de processos existentes.

## Fase 1 - Discovery

Nesta [fase](../sourceFiles/PRP-C-0016.md) foi realizado um trabalho para analisar e mapear o estado atual das operacoes da engenharia global.

Neste momento foi identificado que essa engenharia ja contava com alguns profissionais e que mais vagas ja haviam sido abertas, totalizando 10 profissionais entre projetistas mecanicos e eletricos. Essas contratacoes e dimensionamento de equipe foram baseados em analise de demandas enviadas pelas unidades de negocio elegidas para utilizar este hub.

Na visao do gerente dessa hub global de engenharia, o problema a ser resolvido era:

>[!question] O que deve ser desenvolvido/melhorado para preparar esse time de engenharia para atender a previsao de demanda existente?

Minha funcao nesta fase foi de criar mecanismos para validar essa suposicao do gerente de engenharia e propor acoes de melhoria.

### Global Engineering Hub Business Model
Primeiro passo foi mapear o modelo de negocio do hub global de engenharia junto ao seu gerente.

- A funcao dessa engenharia eh atender a demanda das unidades de negocio de reparos, tanto fabricas quanto unidades de servicos
  - Fabricas de reparos: Oferecem escopos mais complexos de reparos, demandando que o transformador seja reparado dentro da fabrica.
  - Unidade de Servicos: Trabalham com escopos mais simples de reparos ou reforma, normalmente executado no site do cliente.

- Cada *business unit* (clientes) deve fornecer um forecast anual de quantidade de horas a ser disponibilizado pelo hub para que possam consumir mensalmente atraves do pagamento de um fee mensal.

- Os membros desse time de engenharia ficarao espealhados em diversas regioes (regions)

- Nao devem existir preferencias de atendimento entre os membros do hub, ou seja, um membro deve ser capaz de exercer suas atividades para qualquer business unit.

### Product Scopes

Foi analisado a forma como a demanda havia sido definida e esse foi um problema critico levantado pelo gerente de engenharia. Ele disse que havia questionado as unidades de negocio sobre o racional por tras das horas levantadas, mas os responsaveis por essas unidades nao foram capazes de comprovar essas demandas de forma clara.
Apos investigacao, percebi que nao havia clareza nos escopos de servicos que essas unidades de negocio poderiam contratar do hub, e nem o hub tinha clareza dos escopos que seria capaz de oferecer para cada unidade de negocio.

### Operation

Como o modelo de negocio exige que pessoas de diferentes localidades pudesses interagir para desenvolver projetos para unidades de negocio espalhadas pelo mundo, foi verificado como a operacionalizacao disso estava mapeada
Todos os mapas de processos apresentados foram feitos pensando num estado futuro, no mundo ideal, sem demonstrar como os escopos poderiam ser desenvolvidos agora.
Isso causava a frustracao dos stakeholders e clientes pela falta de clareza de quais deveriam ser os outputs do hub e como se daria essa comunicacao/interacao com sues clientes.

### Workshop

Apos essas descobertas, foi sugerido pelos stakeholders de se fazer um workshop para determinar os caminhos a se seguir na continuacao desse projeto.

Os objetivos do workshop foram:

- Discutir e mapear oportunidades de melhoria baseadas na suposicao existente
- Resumir as melhorias em uma problema claro a ser enderecado
- Esbocar caminhos para atingir o target
- Definir um caminho unico para ser prototipado.

As oportunidades de melhoria foram mapeadas no documento "Opportunities_Improvements.xls" dentro do oneDrive.

Apos analisar as melhorias, pude veriricar que tanto os stakeholders do projeto quanto os atores, aqueles responsaveis por executar os processos no dia a dia, nao sabiam responder a seguinte pergunta:

>[!question] Project Question
>When something happens, will we know when to act, what is required, and how to execute it all? 

Para responder essa pergunta foi definido o caminho de desenvolver os standard operational procedures (SOP) para as atividades de cada processo.

>[!HINT] Event-Driven Idea was born
> Durante o workshop pude perceber a dificuldade de gestores e funcionarios em entender a conexao entre a forma de execucao das tarefas do dia a dia com os objetivos e requisitos da organizacao e seus clientes. Essa eh a principal causa por tras do problema a ser resolvido, praticamente todos os envolvidos nesse projeto sempre entraram em empresas onde essa etapa de processos ja estava definida. Mas dado o tempo curto para colocar o hub para atender os clientes, nao ha tempo para formatar uma equipe de qualidade para fazer esse trabalho. Por isso pensei em desenvolver um metodo mais agil e inteligivel para faze-lo

### Prototype 

>[!IMPORTANT] Governanca
> O principal objetivo deste prototipo foi definido neste [documento](./quality_management.md)

Foi Decidido prototipar os SOPs em miscrosoft (sharepoint) lists pois essa eh uma ferramenta amplamente utilizada pelo cliente.

Neste prototipo optei por usar uma [versao simplificada](./EDQMS-Prototype_Diagram.png) da arquitetura do sistema, ja que a ideia nao eh validar o [sistema](./EDQMS-01_DataModel_DesignRationale.md) e sim se com os procedimentos mapeados seriamos capazes de responder a pergunta do projeto

A ideia eh criar os cadastros de events, process, activity, actions, handouts, constrains e procedures para validar a aplicabilidade da lista de procedimentos na solucao do problema apresentado. Abaixo uma lista com as entidades e os respectivos links para acessar as listas sharepoint.


| Entity | Sharepoint List |
| :--- | :--- |
| Event | [event list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JADX-ZYffFWlRIkb4dKSSKkDAS5nW6aGDKdHvVzvvtO_al0?e=bo5Y2e) |
| Process |[process list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JACI7rapl98QToi1CY1Mv5vRAWK84A2DF8c1s_EBeHnSIA4?e=yfd74u)|
| Activity | [activity list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JACI7rapl98QToi1CY1Mv5vRAWK84A2DF8c1s_EBeHnSIA4?e=dzjw1v)|
| Actions | [actions list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JAA4MvW114jGRpj1SuD344sxAZAgi_bq9kiAQv5A49KUif0?e=4eLn00) |
| Handouts | [handouts list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JADxdUgQAQW1SqfRiyW4cS79AYjcPevcLVpDtNl6aoBgDnk?e=x5AQIQ) |
| Constrains | [constrains list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JAArCR49W2rIRIYfTvWLdwppAQNdS1RlNseUsT3FsMjqbv0?e=cgOc1C) |
| Procedures | [procedures list](https://neundesign-my.sharepoint.com/:l:/g/personal/bova_neun-design_com_br/JADX-ZYffFWlRIkb4dKSSKkDAQnnTc27XfiYhtrPo1_MFO8?e=IkhAKm) |


## Fase 2 - Validation 

Esta eh a fase atual do projeto onde iremos validar o prototipo atraves da aplicacao da [auditoria](../sourceFiles/event-audit.md) de um [caso real](../sourceFiles/case-study.md), para verficar se modelo de dados e o template para cadastro de procedimento sao suficientes para responder a pergunta (problema) do projeto.
Este processo foi batizado pelo cliente como end-to-end process avaluation.
Baseado nesta ideia foi desenvolvida a proposta [PRP-C-0017](./Proposal_PRP-C-0017_rev0.md) ja aprovada pelo cliente.

### MVP Assessment
Apos a auditoria e revisao do prototipo, sera feito uma avaliacao para transformar o prototipo em um MVP a ser implementado na proxima fase.

## Fase 3 - Development and implementation  

Apos a validacao do prototipo e mapeamento das melhorias e solucoes necessarias para transformar o prototipo em uma ferramenta que possa ser utilizada na operacao, entra a fase de desenvolvimento e implementacao

Essa fase ainda nao possui proposta pois sera necessario finalizar a fase 2.

