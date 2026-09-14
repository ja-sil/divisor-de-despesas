def cadastrar_participantes() -> list[str]:
    """
    Cadastra os participantes que irão participar do evento.
    A função pergunta a quantidade de participantes e depois
    solicita o nome de cada um. Também verifica se o nome não
    está vazio e se não foi cadastrado anteriormente.

    Retorna:
        list[str]: Lista com os nomes dos participantes cadastrados.
    """

    participantes = []

    qtd = int(input("\nQuantos participantes você deseja cadastrar? "))

    while qtd <= 0:
        print("Por favor, digite um número maior que zero.")
        qtd = int(input("Quantos participantes você deseja cadastrar? "))

    for i in range(1, qtd + 1):
        while True:
            nome = input(f"Informe o nome do {i}º participante: ").strip()

            if not nome:
                print("O nome não pode ser vazio.")

            elif nome in participantes:
                print(
                    "Este participante já foi cadastrado. "
                    "Digite um nome diferente.")

            else:
                participantes.append(nome)
                break

    return participantes


def buscar_participante(
    participantes: list[str],
    numero: int) -> str | None:
    """
    Busca um participante pelo número informado.

    A função é utilizada para encontrar o nome da pessoa
    escolhida pelo usuário através do número apresentado
    na lista de participantes.

    Parâmetros:
        participantes (list[str]): Lista de participantes.
        numero (int): Número escolhido pelo usuário.

    Retorna:
        str | None: Nome do participante encontrado ou None
        caso o número seja inválido.
    """

    if 1 <= numero <= len(participantes):
        return participantes[numero - 1]

    return None