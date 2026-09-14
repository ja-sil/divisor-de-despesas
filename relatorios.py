def exibir_resumo(resultados: dict) -> None:
    """
    Exibe o resumo final das despesas no terminal.

    A função apresenta quanto cada participante pagou,
    o total gasto pelo grupo, o valor médio por pessoa
    e o saldo individual.

    O saldo positivo aparece com o sinal + e representa
    um valor que a pessoa deve receber. O saldo negativo
    representa um valor que a pessoa deve pagar.

    Parâmetros:
        resultados (dict): Resultados obtidos pelos cálculos.

    Retorna:
        None: Apenas apresenta as informações na tela.
    """

    total_grupo = resultados["total_grupo"]
    valor_medio = resultados["valor_medio"]
    pago_por_pessoa = resultados["pago_por_pessoa"]
    saldos = resultados["saldos"]

    print("\n" + "=" * 35)
    print("----RESUMO DAS DESPESAS----")
    print("=" * 35)

    # Mostra quanto cada participante pagou.
    for pessoa, pago in pago_por_pessoa.items():
        print(f"{pessoa} pagou R$ {pago:.2f}")

    print("-" * 35)

    print(f"Total: R$ {total_grupo:.2f}")
    print(f"Valor por pessoa: R$ {valor_medio:.2f}")

    print("-" * 35)

    # Mostra o saldo de cada participante.
    for pessoa, saldo in saldos.items():

        if saldo >= 0:
            print(f"{pessoa}: + R$ {saldo:.2f}")
        else:
            print(f"{pessoa}: - R$ {abs(saldo):.2f}")

    print("=" * 35)