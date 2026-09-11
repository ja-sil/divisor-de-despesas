def registrar_despesas(participantes):
    """Registra as despesas informando pagador, descrição, categoria e valor."""
    despesas = []
    print("\n--- Registro de Despesas ---")

    while True:
        print("\nParticipantes:")
        for idx, nome in enumerate(participantes, 1):
            print(f"  {idx}. {nome}")

        opcao = input(
            "\nDigite o número do pagador (ou '0' para encerrar o lançamento de despesas): "
        ).strip()

        if opcao == "0":
            if not despesas:
                confirmar = input(
                    "Nenhuma despesa registrada. Deseja realmente sair? (s/n): "
                ).lower()
                if confirmar != "s":
                    continue
            break

        try:
            idx_pagador = int(opcao)
            if idx_pagador < 1 or idx_pagador > len(participantes):
                print("Número de participante inválido.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número do menu.")
            continue

        pagador = participantes[idx_pagador - 1]
        descricao = (
            input("Descrição da despesa (ex: Churrasco, Gasolina): ")
            .strip()
            or "Sem descrição"
        )
        categoria = (
            input("Categoria (ex: Alimentação, Transporte, Hospedagem): ")
            .strip()
            or "Geral"
        )

        try:
            valor = float(
                input("Valor pago (R$): ").replace(",", ".").strip()
            )
            if valor <= 0:
                print("O valor precisa ser maior que zero.")
                continue
        except ValueError:
            print("Valor numérico inválido.")
            continue

        despesas.append(
            {
                "pagador": pagador,
                "descricao": descricao,
                "categoria": categoria,
                "valor": valor,
            }
        )
        print(
            f"Despesa de R$ {valor:.2f} ({descricao}) registrada para {pagador}."
        )

    return despesas