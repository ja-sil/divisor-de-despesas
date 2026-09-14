# Relatório de Organização do Projeto – Divisor de Despesas

## 1. Organização do projeto

O projeto foi desenvolvido em Python utilizando a técnica de modularização. A aplicação foi dividida em diferentes arquivos, de forma que cada módulo tenha uma responsabilidade específica.

A estrutura escolhida foi:

```text
divisor_despesas/
│
├── main.py
├── participantes.py
├── despesas.py
├── calculos.py
├── relatorios.py
└── README.md
```

A organização em módulos facilita a compreensão do código, evita que todas as funções fiquem concentradas em um único arquivo e permite que cada parte do sistema seja desenvolvida e modificada de forma independente.

## 2. Responsabilidade de cada módulo

### main.py

O `main.py` é o ponto de entrada da aplicação. Sua principal função é coordenar o funcionamento do sistema.

Ele solicita a quantidade de participantes, chama a função responsável pelo cadastro, recebe as informações das despesas e utiliza as funções dos outros módulos para realizar os cálculos e apresentar os resultados.

Dessa forma, o `main.py` não concentra toda a lógica do programa, funcionando principalmente como coordenador da aplicação.

### participantes.py

O módulo `participantes.py` é responsável pelo cadastro e validação dos participantes.

Ele possui funções para cadastrar os nomes das pessoas que participarão da divisão das despesas e verificar se uma pessoa informada está cadastrada no grupo.

### despesas.py

O módulo `despesas.py` é responsável pelo registro das despesas.

Cada despesa armazenada possui informações sobre:

* participante que realizou o pagamento;
* descrição da despesa;
* valor pago;
* categoria da despesa.

A responsabilidade desse módulo é organizar essas informações e adicioná-las à lista de despesas.

### calculos.py

O módulo `calculos.py` é responsável por realizar os cálculos necessários para a divisão das despesas.

Entre suas funções estão:

* calcular o total gasto pelo grupo;
* calcular o valor médio que cada participante deveria pagar;
* calcular quanto cada participante pagou;
* calcular o saldo individual;
* calcular as transferências entre os participantes.

O saldo é calculado comparando o valor que a pessoa pagou com o valor que deveria pagar. Quando o saldo é positivo, a pessoa tem dinheiro a receber. Quando o saldo é negativo, a pessoa precisa pagar.

### relatorios.py

O módulo `relatorios.py` é responsável pela apresentação dos resultados no terminal.

Ele exibe as despesas cadastradas, o total pago por cada participante, o total gasto pelo grupo, o valor por pessoa, os saldos individuais e as transferências necessárias.

Esse módulo recebe os resultados dos cálculos realizados pelo `calculos.py`, não sendo responsável por realizar as operações matemáticas.

Além disso, a função `formatar_moeda()` foi colocada neste módulo para formatar os valores monetários e é reutilizada pelas outras funções de relatório.

## 3. Modularização

A modularização foi utilizada para separar as responsabilidades do sistema. Assim, cada arquivo possui uma finalidade definida.

Por exemplo, caso seja necessário modificar a forma como os cálculos dos saldos são realizados, a alteração pode ser feita no `calculos.py` sem precisar modificar as funções responsáveis pelo cadastro ou pela apresentação dos resultados.

Essa separação também torna o código mais organizado e facilita sua manutenção.

## 4. Reu
