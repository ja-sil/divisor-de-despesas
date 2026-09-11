def cadastrar_participantes():
    participantes = []

    while True:
        try:
            qtd = int(input("Quantos participantes você deseja cadastrar? "))
            if qtd > 0:
                break
            print("Por favor digite um número maior que zero")
        except ValueError:
            print("Entrada inválida! tente novamente")

    for i in range(1, qtd + 1):
        while True:
            nome = input(f"Informe o nome do {i}º participante: ").strip()
            if not nome:
                print("O nome não pode ser vazio")
            elif nome in participantes:
                print("Este participante já foi cadastrado. Digite um nome diferente.")
            else:
                participantes.append(nome)
                break

    return participantes