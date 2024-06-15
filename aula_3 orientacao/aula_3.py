# def soma():
#     numero = int(input(':'))
#     if numero >10:
#         print('E maior')
#     else:
#         print(' e menor ou igual a 10')
# def subtracao():
#     print(10-5)

# subtracao()
# soma()

def soma():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    soma = n1 + n2
    print('=', soma)
def subtracao():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    subtracao = n1 - n2
    print('=', subtracao)
def multiplicacao():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    multiplicacao = n1 * n2
    print('=', multiplicacao)
def divisao():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    divisao = n1 / n2
    print('=', divisao)

def calculadora():
    escolha  = input('(+) (-) (*) (/)')
    if escolha == '+':
        soma()
    elif escolha == '-':
        subtracao()
    elif escolha == '*':
        multiplicacao()
    elif escolha == '/':
        divisao()
    else:
        print('Opcao invalida')

calculadora()