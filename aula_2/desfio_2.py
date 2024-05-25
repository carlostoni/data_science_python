# Crie um sistema de Banco, onde o usuário pode digitar a senha apenas 3 x, após isso existirá o bloqueio do sistema.  

# saque (subtração)

# deposito(soma)

# visualizar o valor em conta (print())

saldo = [200]
saque = []
deposito = []

user = 'carlos'
password = 1234


for n in range(1,4):
    nome = input('digite o nome de usuario: ')
    senha = int(input('digite sua senha: '))
    
    if user == nome and password == senha:
        
        print('Autorizado')
        print(f'''oque deseja fazer:
        1- saldo
        2- saque
        3- deposito''')
        modo = int(input('digite a opcao '))
        if modo == 1:
            print(f'o saldo disponivel e: {saldo}')
        elif modo == 2:
            saque = int(input('digite o valor que deseja sacar: '))
            if saldo[0] < saque:
                print('saldo insuficiente')
                break
            else:
                total = saldo[0] - saque
                print(total)
                break
        elif modo == 3:
            deposito = int(input('digite o valor que deseja depositar: '))
            if deposito > 0:
                saldo.append(deposito)
                soma = sum(saldo)
                print(f'saldo em conta {soma}')
                break

    else:
        if n == 3:
            print('tentativas esgotadas')