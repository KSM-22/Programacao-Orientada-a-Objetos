cpf = str
def VerificarCPF(cpf):
    while True:
        while True:
            cpf = input('Digite o CPF: ')
            cpf = cpf.replace('.', '').replace('-', '')
            if not cpf.isdigit():
                print('Caracteres invalidos!')
                continue
            if  len(cpf) < 11:
                print('Há números faltando!')
                continue
            elif len(cpf) > 11:
                print('Há números demais')
                continue
            else:
                break

        tabela = list(map(int, cpf))
        soma1 = 10 * tabela[0] + 9 * tabela[1] + 8 * tabela[2] + 7 * tabela[3] + 6 * tabela[4] + 5 * tabela[5] + 4 * tabela[6] + 3 * tabela[7] + 2 * tabela[8]
        resto1 = soma1 % 11
        numero10 = 11 - resto1
        if resto1 < 2:
            numero10 = 0
        soma2 = 11 * tabela[0] + 10 * tabela[1] + 9 * tabela[2] + 8 * tabela[3] + 7 * tabela[4] + 6 * tabela[5] + 5 * tabela[6] + 4 * tabela[7] + 3 * tabela[8] + 2 * tabela[9]
        resto2 = soma2 % 11
        numero11 = 11 - resto2
        if resto2 < 2:
            numero11 = 0
        if numero10 == tabela[9] and numero11 == tabela[10]:
            print('Cpf = Valido')
            break
        else:
            print('Cpf = Invalido')
            continue            




VerificarCPF(cpf)
