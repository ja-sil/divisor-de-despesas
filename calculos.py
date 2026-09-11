def calcular_totais_e_saldos(participantes, despesas):
    """Calcula o total geral, gasto por pessoa, valor médio e o saldo individual.

    - Saldo positivo (+): a pessoa pagou a mais e deve RECEBER.
    - Saldo negativo (-): a pessoa pagou a menos e deve PAGAR.
    """
    total_grupo = sum(d["valor"] for d in despesas)
    qtd_participantes = len(participantes)
    valor_medio = total_grupo / qtd_participantes if qtd_participantes > 0 else 0.0

    pago_por_pessoa = {p: 0.0 for p in participantes}

    for d in despesas:
        pago_por_pessoa[d["pagador"]] += d["valor"]

    saldos = {p: pago_por_pessoa[p] - valor_medio for p in participantes}

    return {
        "total_grupo": total_grupo,
        "valor_medio": valor_medio,
        "pago_por_pessoa": pago_por_pessoa,
        "saldos": saldos,
    }