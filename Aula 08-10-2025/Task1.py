def perguntas():
    while True:
        nome = str(input('Digite seu nome: '))

        if not nome.isascii():
            print('Só é aceito letras!\n')
            continue

        nome = nome.split(' ')

        if len(nome) < 2:
            print('Nome insuficiente!\n')
            continue

        else:
            nome = ' '.join(nome)
            break



    while True:
        idade = str(input('Digite sua idade: '))

        if not idade.isdigit():
            print('Só é aceito números!\n')
            continue

        idade = int(idade)
        if idade < 0 or idade > 125:
            print('Idade irreal:!\n')
            continue

        else:
            break

    while True:
        altura = input('Digite sua altura: ')

        if not altura.isdigit():
            print('Só é aceito números!\n')
            continue

        altura = float(altura)

        if altura < 0 or altura > 3:
            print('altura irreal!\n')

        else:
            break
    while True:
        peso = input('Digite seu peso: ')

        if not peso.isdigit():
            print('Peso irreal!\n')
            continue

        peso = float(peso)
        if peso < 0 or peso > 500:
            print('Peso irreal!\n')
            continue

        else:
            break

    while True:
        nacionalidade = input('Digite seu nacionalidade: ')

        if not nacionalidade.isalpha():
            print('Só é aceito letras!\n')
            continue

        else:
            break
    print(f'Meu nome é {nome}, tenho {idade} anos e {altura} metros,'
          f' tenho {peso} kilos e sou {nacionalidade}.')

perguntas()
