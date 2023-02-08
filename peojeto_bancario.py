menu = '''
----------------
[1] Depositar  
[2] Sacar      
[3] Extrato    
[0] Sair       
----------------
'''

saldo = 0
limite = 500
numero_saques = 0
extrato = ''
LIMITE_SAQUES = 5

while True:
    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Informe o valor a ser depositado: '))

        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
        else:
            print('Operação inválida! O valor desejado não é válido')

    elif opcao == '2':
        deposito = float(input('Informe o valor a ser sacado: '))
        excedeu_saldo = deposito > saldo
        excedeu_limite = deposito > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Falha! Saldo insuficiente!')
        elif excedeu_limite:
            print('Falha! O valor do saque atingiu o limite!')
        elif excedeu_saques:
            print('Falha! Você atingiu o número máximo de saques!')
        elif deposito > 0:
            saldo -= deposito
            extrato += f'Saques: R$ {deposito:.2F}\n'
            numero_saques += 1
        else:
            print('O valor é inválido!')
    
    elif opcao == '3':
        print('\n---------------Extrato---------------')
        print('Sem movimentações!' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('-------------------------------------')

    elif opcao == '0':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')