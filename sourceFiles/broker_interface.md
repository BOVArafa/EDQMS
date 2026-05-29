--- 
content-type: instruction
subject: 
  - datamodel
  - method
  - concept
--- 

# Definition
A conexao entre logica/regras de negocio, requisitos, riscos e oportunidades (payload) aos eventos, deve ser feita atraves de um broker. -> responsavel por definir a heuristica do comportamento do processo.


Essa deve ser uma nova funcao (role) dentro do sistema de gestao da qualidade assim como uma interface (classe assossiativa) no modelo de dados.

## Payload - Association Class

A entidade `payload` sera utilizada para armazenar os atributos a serem aplicados pelo [fluxo de controle](˜/Users/rafaelbova/Vaults/techdocs/Books/Fundamentals_of_Business_Process_Managemen_-_Jan_Mendling_Marlon_Dumas_Marcello_La_Ros.pdf) de cada  processo.
Ou seja, a combinacao de um evento com requisitos e specs de produto pode disparar varios processos ou uma unica atividade.
A process is composed of multiple activities. Therefore, a single payload cannot trigger more than one activity. To initiate multiple activities, the payload must instead trigger a process that orchestrates and connects those activities

## Broker - Role
Este papel pode ser absorvido pelo process owner ou process manager, mas o ideal eh que seja realizado por alguem com uma visao total dos processos, como o gerente da qualidade ou alguem abaixo dele.

A funcao deste papel eh criar payloads e conecta-los a atividades ou processos, ou seja, definir as regras de negocio que conectarao as duas entidades.

# Relationship Rules

- Um evento pode disparar um ou mais processos OU zero ou uma atividade
- Um unico evento NUNCA podera disparar um processo e uma atividade simultaneamente
- Uma atividade pode conter zero ou um payload (#datamodel/0002)

