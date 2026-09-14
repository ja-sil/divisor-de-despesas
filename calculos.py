def calcular_totais_e_saldos(
    participantes: list[str],
    despesas: list[dict]) -> dict:
    """
    Calcula os valores das despesas do grupo.
    A função calcula o total gasto, quanto cada participante
    pagou, o valor médio que cada pessoa deveria pagar e
    o saldo individual.

    Quando o saldo é positivo, significa que a pessoa pagou
    mais do que deveria e deve receber. Quando é negativo,
    significa que a pessoa deve pagar.

    Parâmetros:
        participantes (list[str]): Lista dos participantes.
        despesas (list[dict]): Lista das despesas registradas.

    Retorna:
        dict: Dicionário contendo os totais, pagamentos e saldos.
    """

    # Soma o valor de todas as despesas.
    total_grupo = sum(
        d["valor"] for d in despesas)

    # Verifica quantas pessoas participarão da divisão.
    qtd_participantes = len(participantes)

    # Calcula o valor que cada pessoa deveria pagar.
    if qtd_participantes > 0:
        valor_medio = total_grupo / qtd_participantes
    else:
        valor_medio = 0.0

    # Cria um valor inicial de R$ 0,00 para cada participante.
    pago_por_pessoa = {
        pessoa: 0.0 for pessoa in participantes
    }

    # Soma quanto cada participante realmente pagou.
    for despesa in despesas:
        pagador = despesa["pagador"]
        valor = despesa["valor"]

        pago_por_pessoa[pagador] += valor

    # Calcula a diferença entre o que foi pago
    # e o valor que cada pessoa deveria pagar.
    saldos = {}

    for pessoa in participantes:
        saldos[pessoa] = (
            pago_por_pessoa[pessoa] - valor_medio
        )

    return {
        "total_grupo": total_grupo,
        "valor_medio": valor_medio,
        "pago_por_pessoa": pago_por_pessoa,
        "saldos": saldos
    }