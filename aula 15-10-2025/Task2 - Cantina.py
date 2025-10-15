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
def MostrarEstoque(sagaldos,bebidas):
    print(f'Salgados:\n{sagaldos}\n\nBebidas:\n{bebidas}')

def AdicionarAlimento():
    print("1. Salgados"
          "2. Bebidas")
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
                else:
                    break
            break

def RemoverAlimento():
    print("""
        1. Salgados
            2. Bebidas
          3. Cancelar""")
    opc = int(input())

def Menu():
    print("Bebidas:""")
AdicionarAlimento()