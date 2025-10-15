bebidas = {
    "Bebida gaseificada saborizada": 35,
    "Bebida saborizada de frutas": 22,
    "Bebida de mistura lactea saborizada de caucau": 18,
    "Bebida não saborizada": 41,
    "Bebida saborizada de frutas tropicais": 30,
    "Bebida saborizada de folhas de grama com corante verde": 16,
    "Bebida com corante preto com cafeina": 28,
    "Bebida de mistura lactea com aditivos de vitaminas não mineirais mechida saborizada de frutas tropicais": 19,
    "Bebida de mistura lactea com fermentação de bactérias lactobacillus": 25,
    "Energético": 12
}


salgados = {
    "Pão de queijo": 40,
    "Coxinha": 32,
    "Salgado de Misto": 27,
    "Empada": 15,
    "Pastel": 22,
    "Kibe": 18,
    "Esfiha": 26,
    "Enroladinho de salsicha": 30,
    "Bolinha de queijo": 24,
    "Torta salgada": 20
}

def MostrarEstoque(salgados,bebidas):
    print(f'Salgados:\n{salgados}\n\nBebidas:\n{bebidas}')


def AdicionarAlimento():
    print("""
        1. Salgados
        2. Bebidas
        3. Cancelar
        """)
    while True:
        opc = int(input())

        if opc == 1:
            while True:
                nome = input("Digite o nome do Salgado: ").capitalize()
                if not nome.isalpha():
                    print("Nome do Salgado invalido!")
                    continue
                while True:
                    salgados[f'{nome}'] = int(input(f"Digite a quantidade de {nome} no estoque: "))
                    if list(salgados.values())[-1] < 0:
                        print('Número invalido')
                        while True:
                            ultimachave = list(salgados.keys())[-1]
                            salgados[ultimachave] = int(input(f"Digite a quantidade de {nome} no estoque: "))
                            if list(salgados.values())[-1] < 0:
                                continue
                            else:
                                break
                            break
                        break
                    else:
                        break
                break
            break

        elif opc == 2:
            while True:
                nome = input("Digite o nome da Bebida: ").capitalize()
                if not nome.isalpha():
                    print("Nome da Bebida invalido!")
                    continue
                while True:
                    bebidas[f'{nome}'] = int(input(f"Digite a quantidade de {nome} no estoque: "))
                    if list(bebidas.values())[-1] < 0:
                        print('Número invalido')
                        while True:
                            ultimachave = list(bebidas.keys())[-1]
                            bebidas[ultimachave] = int(input(f"Digite a quantidade de {nome} no estoque: "))
                            if list(bebidas.values())[-1] < 0:
                                continue
                            else:
                                break
                        break
                    else:
                        break
                break
            break

        elif opc == 3:
            break

        else:
            print("Digite apenas | 1 | 2 | 3 |:")
            continue

def RemoverAlimento(salgados, bebidas):
    print("""
        1. Salgados
        2. Bebidas
        3. Cancelar""")

    while True:
        try:
            opc = int(input("Escolha a opção: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if opc == 1:
            print(f"Salgados em estoque:\n{list(salgados.keys())}\n")
            while True:
                nome_produto = input('Qual o NOME exato do salgado para retirar do estoque? ')

                if nome_produto not in salgados:
                    print(f"'{nome_produto}' não encontrado na lista de Salgados. Tente novamente.")
                    continue

                try:
                    quantidade_remover = int(input(
                        f"Quantas unidades de '{nome_produto}' deseja remover (Estoque atual: {salgados[nome_produto]})? "))
                except ValueError:
                    print("Quantidade inválida. Digite apenas números inteiros.")
                    continue

                if quantidade_remover <= 0:
                    print("A quantidade a remover deve ser maior que zero.")
                    continue

                estoque_atual = salgados[nome_produto]

                if quantidade_remover > estoque_atual:
                    print(
                        f"ERRO: Você está tentando remover {quantidade_remover}, mas só há {estoque_atual} em estoque. ")
                    continue

                novo_estoque = estoque_atual - quantidade_remover
                salgados[nome_produto] = novo_estoque

                print(f"Sucesso! {quantidade_remover} unidades de {nome_produto} vendidas/removidas.")

                if novo_estoque == 0:
                    del salgados[nome_produto]
                    print(f"O estoque de '{nome_produto}' chegou a zero e o item foi removido da lista.")
                    break
                else:
                    print(f"Novo estoque de {nome_produto}: {novo_estoque} unidades.")
                    break
                break
            break

        elif opc == 2:
            print(f"Bebidas em estoque:\n{list(bebidas.keys())}\n")
            while True:
                nome_produto = input('Qual o NOME exato da bebida para retirar do estoque? ')

                if nome_produto not in bebidas:
                    print(f"'{nome_produto}' não encontrado na lista de Bebidas. Tente novamente.")
                    continue

                try:
                    quantidade_remover = int(input(
                        f"Quantas unidades de '{nome_produto}' deseja remover (Estoque atual: {bebidas[nome_produto]})? "))
                except ValueError:
                    print("Quantidade inválida. Digite apenas números inteiros.")
                    continue

                if quantidade_remover <= 0:
                    print("A quantidade a remover deve ser maior que zero.")
                    continue

                estoque_atual = bebidas[nome_produto]

                if quantidade_remover > estoque_atual:
                    print(
                        f"ERRO: Você está tentando remover {quantidade_remover}, mas só há {estoque_atual} em estoque. ")
                    continue

                novo_estoque = estoque_atual - quantidade_remover
                bebidas[nome_produto] = novo_estoque

                print(f"Sucesso! {quantidade_remover} unidades de {nome_produto} vendidas/removidas.")

                if novo_estoque == 0:
                    del bebidas[nome_produto]
                    print(f"O estoque de '{nome_produto}' chegou a zero e o item foi removido da lista.")
                    break
                else:
                    print(f"Novo estoque de {nome_produto}: {novo_estoque} unidades.")
                    break
                break
            break

        elif opc == 3:
            print("Operação cancelada.")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

def ConsultarBebidas(salgados, bebidas):
    produto = input("Digite o nome exato do produto que deseja consultar no estoque: ").capitalize()

    if produto in bebidas:
        quantidade = bebidas[produto]
        print(f"O produto '{produto}' é uma BEBIDA e a quantidade atual em estoque é: {quantidade} unidades.")

    elif produto in salgados:
        quantidade = salgados[produto]
        print(f"O produto '{produto}' é um SALGADO e a quantidade atual em estoque é: {quantidade} unidades.")

    else:
        print(f"O produto '{produto}' não foi encontrado no estoque de bebidas ou salgados.")

def SalvarRelatorio():
    contador = 1

    with open(f"Relatorio{contador}.txt", "w") as arquivo:
        arquivo.write(f"Salgados:\n{salgados}\n\nBebidas:\n{bebidas}")
    print("Relatorio Criado!")

    contador = contador + 1

def ReporAutomatico(salgados, bebidas):
    itens_repostos = []

    for nome, quantidade in salgados.items():
        if quantidade <= 2:
            salgados[nome] += 5
            itens_repostos.append((nome, quantidade, salgados[nome], "Salgado"))

    for nome, quantidade in bebidas.items():
        if quantidade <= 2:
            bebidas[nome] += 5
            itens_repostos.append((nome, quantidade, bebidas[nome], "Bebida"))

    print("\nReposição Automática Concluída")

def Menu(salgados, bebidas):
    while True:
        print("""
    1. Mostrar Estoque
    2. Adicionar Alimento
    3. Remover Alimento
    4. Consultar Bebidas
    5. Salvar Relatorio
    6. Repor Automatico
    7. Sair
    """)
        try:
            opc = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opc == 1:
            MostrarEstoque(salgados, bebidas)
        elif opc == 2:
            AdicionarAlimento()
        elif opc == 3:
            RemoverAlimento(salgados, bebidas)
        elif opc == 4:
            ConsultarBebidas(salgados, bebidas)
        elif opc == 5:
            SalvarRelatorio()
        elif opc == 6:
            ReporAutomatico(salgados, bebidas)
        elif opc == 7:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 7.")

Menu(salgados, bebidas)

