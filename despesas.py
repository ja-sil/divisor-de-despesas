from participantes import buscar_participante

def registrar_despesas(participantes: list[str]) -> list[dict]:
    """
    Registra as despesas realizadas durante o evento.

    A função apresenta os participantes cadastrados e permite
    informar quem realizou cada pagamento, sua descrição,
    categoria e valor.

    O cadastro de despesas continua até que o usuário escolha
    a opção 0 para encerrar.

    Parâmetros:
        participantes (list[str]): Lista de participantes cadastrados.

    Retorna:
        list[dict]: Lista contendo as despesas registradas.
    """

    despesas = []

    print("\n--- Registro de Despesas ---")

    while True:
        print("\nParticipantes:")

        for idx, nome in enumerate(participantes, 1):
            print(f"  {idx}. {nome}")

        opcao = input(
            "\nDigite o número do pagador "
            "(ou '0' para encerrar): ").strip()

        if opcao == "0":

            if not despesas:
                confirmar = input(
                    "Nenhuma despesa registrada. "
                    "Deseja realmente sair? (s/n): ").lower()

                if confirmar != "s":
                    continue

            break

        idx_pagador = int(opcao)

        # Utiliza uma função criada no módulo participantes.
        pagador = buscar_participante(
            participantes,idx_pagador)

        if pagador is None:
            print("Número de participante inválido.")
            continue

        descricao = input("Descrição da despesa (ex: Churrasco, Gasolina):").strip()

        if not descricao:
            descricao = "Sem descrição"

        categoria = input("Categoria da despesa (ex: Alimentação, Transporte, Hospedagem):").strip()

        if not categoria:
            categoria = "Geral"

        valor = float(input("Valor pago (R$): ")
            .replace(",", "."))

        if valor <= 0:
            print("O valor precisa ser maior que zero.")
            continue

        despesas.append(
            {
                "pagador": pagador,
                "descricao": descricao,
                "categoria": categoria,
                "valor": valor
            }
        )

        print(
            f"Despesa de R$ {valor:.2f} "
            f"({descricao}) registrada para {pagador}.")

    return despesas