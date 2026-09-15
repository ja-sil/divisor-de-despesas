from participantes import cadastrar_participantes
from despesas import registrar_despesas
from calculos import calcular_totais_e_saldos
from relatorios import exibir_resumo

def main() -> None:
    """
    Executa o fluxo principal do sistema.

    A função organiza a execução das etapas do programa:
    cadastro dos participantes, registro das despesas,
    cálculo dos valores e apresentação do relatório final.

    Retorna:
        None: Apenas coordena a execução do programa.
    """

    print("\n---- SISTEMA DE DIVISÃO DE DESPESAS DA TURMA ----")

    # Cadastra os participantes.
    participantes = cadastrar_participantes()

    # Registra as despesas do evento.
    despesas = registrar_despesas(participantes)

    # Realiza os cálculos das despesas e dos saldos.
    resultados = calcular_totais_e_saldos(
        participantes,despesas)

    # Exibe o resumo final para o usuário.
    exibir_resumo(resultados)


if __name__ == "__main__":
    main()