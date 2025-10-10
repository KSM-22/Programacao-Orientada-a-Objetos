

def menu():
    saldo = 1000
    historico = []
    contador = 1
    while True:
        print('+' + 'Caixa Eletronico'.center(50,'-') + '+')
        print('|' + (' ' * 10) + '1 - Depositar'.ljust(40) + '|')
        print('|' + (' ' * 10) + '2 - Sacar'.ljust(40) + '|')
        print('|' + (' ' * 10) + '3 - Ver Saldo'.ljust(40) + '|')
        print('|' + (' ' * 10) + '4 - Ver Histórico de Transações'.ljust(40) + '|')
        print('|' + (' ' * 10) + '5 - Sair'.ljust(40) + '|')

        opc = input((' ' * 11) + 'Digite: ')
        if opc == '1':
            deposito = int(
                input('+' + 'Depositar'.center(50, '-') + '+' + '\n' + (' ' * 11) + 'Faça seu Deposito (R$): '))
            saldo = saldo + deposito
            historico.append(f'+{deposito}')
            continue
        if opc == '2':
            saque = int(input('+' + 'Sacar'.center(50, '-') + '+' + '\n' + (' ' * 11) + 'Faça seu Saque (R$): '))
            saldo = saldo - saque
            historico.append(f'-{saque}')
            continue
        if opc == '3':
            print('+' + 'Ver Saldo'.center(50, '-') + '+' + '\n' + '|' + (' ' * 10) + f'Seu saldo é: {saldo}'.ljust(40) + '|')

            continue
        if opc == '4':
            print('+' + 'Ver Histórico de Transações'.center(50, '-') + '+')
            for movimentacao in historico:
                print('|' + (' ' * 10) + f'{contador} - {movimentacao}'.ljust(40) + '|')
                contador = contador + 1
            continue
        if opc == '5':
            break

menu()