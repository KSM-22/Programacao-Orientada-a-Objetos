contador = 1
contador_lados = -1
coordenadas = []
lados = []
sair = False

def menu():
    poligonos = {
        "Triângulo Equilátero": [(0, 0), (1, 0), (0.5,0.87)],
        "Triângulo Isósceles": [(0, 0), (2, 0), (1, 1)],
        "Triângulo Escaleno": [(0, 0), (5, 0), (3, 2)],
        "Quadrado": [(0, 0), (0, 4), (4, 4), (4, 0)],
        "Retângulo":[(0, 0), (0, 2,), (4, 2), (4, 0)],
        "Pentágono": [(1.0, 0.0), (0.31, 0.95), (-0.81, 0.59), (-0.81, -0.59), (0.31, -0.95)],
        "Hexágono": [(1.0, 0.0), (0.5, 0.87), (-0.5, 0.87), (-1.0, 0.0), (-0.5, -0.87), (0.5, -0.87)],
        "Heptágono": [(1.0, 0.0), (0.62, 0.78), (0.17, 0.98), (-0.45, 0.89), (-0.91, 0.43), (-0.91, -0.43), (-0.45, -0.89)],
        "Octógono": [(1.0, 0.0), (0.71, 0.71), (0.0, 1.0), (-0.71, 0.71), (-1.0, 0.0), (-0.71, -0.71), (0.0, -1.0), (0.71, -0.71)],
        "Eneágono": [(1.0, 0.0), (0.77, 0.64), (0.17, 0.98), (-0.5, 0.87), (-0.94, 0.34), (-0.94, -0.34), (-0.5, -0.87), (0.17, -0.98), (0.77, -0.64)],
        "Decágono": [(1.0, 0.0), (0.81, 0.59), (0.31, 0.95), (-0.31, 0.95), (-0.81, 0.59), (-1.0, 0.0), (-0.81, -0.59), (-0.31, -0.95), (0.31, -0.95), (0.81, -0.59)],
        "Undecágono": [(1.0, 0.0), (0.84, 0.54), (0.42, 0.91), (-0.14, 0.99), (-0.65, 0.76), (-0.9, 0.43), (-0.9, -0.43), (-0.65, -0.76), (-0.14, -0.99), (0.42, -0.91), (0.84, -0.54)],
        "Dodecágono": [(1.0, 0.0), (0.87, 0.5), (0.5, 0.87), (0.0, 1.0), (-0.5, 0.87), (-0.87, 0.5), (-1.0, 0.0), (-0.87, -0.5), (-0.5, -0.87), (0.0, -1.0), (0.5, -0.87), (0.87, -0.5)]}

    while True:
        print("\n===== MENU DE POLÍGONOS =====")
        print("1 - Ver exemplo de um polígono")
        print("2 - Criar polígono manualmente")
        print("3 - Gerar polígono de exemplo")
        print("4 - Sair")
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            nomes = list(poligonos.keys())
            print("\nEscolha o polígono pelo número:")
            for i, nome in enumerate(nomes, start=1):
                print(f"{i}. {nome}")

            while True:
                try:
                    opc = int(input("Digite o número do polígono desejado: "))
                    if 1 <= opc <= len(nomes):
                        nome_escolhido = nomes[opc - 1]
                        print(f"\nExemplo de coordenadas para {nome_escolhido}:")
                        for ponto in poligonos[nome_escolhido]:
                            print(ponto)
                        break
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Digite apenas números inteiros.")

        elif escolha == "2":
            print("\n=== Criar polígono manualmente ===")
            print("Digite as coordenadas dos vértices. Mínimo de 3 vértices necessários.")
            try:
                iniciar()
            except Exception as e:
                print(f"Erro ao criar polígono: {e}")
                continue

        elif escolha == "3":
            criar_poligono(poligonos)
        elif escolha == "4":
            print("Saindo do menu...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def criar_poligono(poligonos):
    global coordenadas, lados
    nomes = list(poligonos.keys())
    print("\nEscolha o polígono pelo número:")
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome}")

    while True:
        try:
            opc = int(input("Digite o número do polígono desejado: "))
            if 1 <= opc <= len(nomes):
                nome_escolhido = nomes[opc - 1]
                coordenadas = [list(ponto) for ponto in poligonos[nome_escolhido]]
                for i in range(len(coordenadas)):
                    if i < len(coordenadas) - 1:
                        lados.append(round(((coordenadas[i][0] - coordenadas[i + 1][0]) ** 2 + (coordenadas[i][1] - coordenadas[i + 1][1]) ** 2) ** 0.5, 2))
                lados.append(round(((((coordenadas[0][0] - coordenadas[-1][0]) ** 2) + (coordenadas[0][1] - coordenadas[-1][1]) ** 2) ** 0.5 * (((coordenadas[0][0] - coordenadas[-1][0]) ** 2) + (coordenadas[0][1] - coordenadas[-1][1]) ** 2) ** 0.5) ** 0.5, 2))
                verificar(lados)
                print(' | '.join([f'Lado {i + 1} - {lado:.2f}' for i, lado in enumerate(lados)]))
                coordenadas.clear()
                lados.clear()
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Digite apenas números inteiros.")

def inserir():
    global contador, coordenadas
    while True:
        inserir = (input(f"{contador}ª vertice do poligono(X,Y): "))
        try:
            x_str, y_str = inserir.split(',')
            x, y = float(x_str), float(y_str)
        except Exception:
            print('Você digitou algo errado, tente novamente nesse formato (X,Y)')
            continue
        if [x, y] in coordenadas:
            print("Essa coordenada já foi inserida. Tente outra.")
            continue
        coordenadas.append([x, y])
        contador += 1

        break


def lado():
    global contador_lados, lados, coordenadas
    contador_lados = contador_lados + 1
    if len(coordenadas) >= 2:
        lados.append(round((((((coordenadas[-2][0] - coordenadas[-1][0]) ** 2) + (coordenadas[-2][1] - coordenadas[-1][1]) ** 2) ** 0.5 * (((coordenadas[-2][0] - coordenadas[-1][0]) ** 2) + (coordenadas[-2][1] - coordenadas[-1][1]) ** 2) ** 0.5)) ** 0.5,2))


def verificar(lados):
    if len(lados) == 3:
        if lados[0] == lados[1] and lados[1] == lados[2]:
            print('O polígono é um triangulo equilátero')
        if lados[0] == lados[1] and lados[0] != lados[2] or lados[2] == lados[1] and lados[2] != lados[0] or lados[0] == lados[2] and lados[0] != lados[1]:
            print('O polígono é um triangulo isósceles')
        if lados[0] != lados[1] and lados[2] != lados[1] and lados[0] != lados[1]:
            print('O polígono é um triangulo escaleno')

    if len(lados) == 4:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3]:
            print('O polígono é um quadrado')
        elif lados[0] == lados[2] and lados[1] == lados[3] and lados[0] != lados[1]:
            print('O polígono é um retângulo')
        else:
            print('O polígono é um quadrilátero irregular ')

    if len(lados) == 5:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4]:
            print('O polígono é um pentágono regular')
        else:
            print('O polígono é um pentágono irregular')
    if len(lados) == 6:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5]:
            print('O polígono é um hexágono regular')
        else:
            print('O polígono é um hexágono irregular')

    if len(lados) == 7:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6]:
            print('O polígono é um heptágono regular')
        else:
            print('O polígono é um heptágono irregular')

    if len(lados) == 8:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6] and lados[6] == lados[7]:
            print('O polígono é um octágono regular')
        else:
            print('O polígono é um octágono irregular')

    if len(lados) == 9:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6] and lados[6] == lados[7] and lados[7] == lados[8]:
            print('O polígono é um nonágono regular')
        else:
            print('O polígono é um nonágono irregular')

    if len(lados) == 10:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6] and lados[6] == lados[7] and lados[7] == lados[8] and lados[8] == lados[9]:
            print('O polígono é um decágono regular')
        else:
            print('O polígono é um decágono irregular')

    if len(lados) == 11:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6] and lados[6] == lados[7] and lados[7] == lados[8] and lados[8] == lados[9] and lados[9] == lados[10]:
            print('O polígono é um hendecágono regular')
        else:
            print('O polígono é um hendecágono irregular')

    if len(lados) == 12:
        if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3] and lados[3] == lados[4] and lados[4] == lados[5] and lados[5] == lados[6] and lados[6] == lados[7] and lados[7] == lados[8] and lados[8] == lados[9] and lados[9] == lados[10] and lados[10] == lados[11]:
            print('O polígono é um dodecágono regular')
        else:
            print('O polígono é um dodecágono irregular')


def iniciar():
    global contador, contador_lados, coordenadas, lados, sair
    while True:
        inserir()
        lado()
        if len(coordenadas) > 2:
            while True:
                perguntar = input("Deseja inserir mais um vertice? (S/N): ").lower()
                if perguntar == 'n' or perguntar == 'não' or perguntar == 'nao' or perguntar == 'no':
                    contador = 1
                    contador_lados = -1
                    sair = True
                    break
                elif perguntar == 's' or perguntar == 'sim' or perguntar == 'yes':
                    sair = False
                    break
                else:
                    print('Você digitou algo errado, tente novamente:')
                    continue
            if sair:
                lados.append(round((((((coordenadas[0][0] - coordenadas[-1][0]) ** 2) + (coordenadas[0][1] - coordenadas[-1][1]) ** 2) ** 0.5 * (((coordenadas[0][0] - coordenadas[-1][0]) ** 2) + (coordenadas[0][1] - coordenadas[-1][1]) ** 2) ** 0.5)) ** 0.5,2))

                break
    verificar(lados)
    coordenadas.clear()
    lados.clear()


menu()
