from participantes import cadastrar_participantes
from despesas import registrar_despesas
from calculos import calcular_totais_e_saldos
from relatorios import exibir_resumo


def main():
    print("---- SISTEMA DE DIVISÃO DE DESPESAS DA TURMA ----")

    #Cadastrar as pessoas
    participantes = cadastrar_participantes()

    #Registrar cada despesa informando pagador, descrição, categoria e valor
    despesas = registrar_despesas(participantes)

    #Processar os valores, calcular os saldos
    resultados = calcular_totais_e_saldos(participantes, despesas)

    #Apresentar o resumo
    exibir_resumo(resultados)


if __name__ == "__main__":
    main()