def exibir_resumo(resultados):
    """Exibe no terminal o extrato de pagamentos, totais e saldos finais."""
    total_grupo = resultados["total_grupo"]
    valor_medio = resultados["valor_medio"]
    pago_por_pessoa = resultados["pago_por_pessoa"]
    saldos = resultados["saldos"]

    print("\n" + "=" * 35)
    print("      RESUMO DAS DESPESAS")
    print("=" * 35)

    for pessoa, pago in pago_por_pessoa.items():
        print(f"{pessoa} pagou R$ {pago:.2f}")

    print("-" * 35)
    print(f"Total: R$ {total_grupo:.2f}")
    print(f"Valor por pessoa: R$ {valor_medio:.2f}")
    print("-" * 35)

    for pessoa, saldo in saldos.items():
        if saldo >= 0:
            print(f"{pessoa}: + R$ {saldo:.2f}")
        else:
            print(f"{pessoa}: - R$ {abs(saldo):.2f}")

    print("=" * 35)