def soma(n1, n2):
    soma = n1 + n2
    return soma

def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

def divisao(n1, n2):
    divisao = n1 / n2
    return divisao

def calculadora():
    escolha  = input('(+) (-) (*) (/)')
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    if escolha == '+':
       soma(n1, n2)

    elif escolha == '-':
        subtracao(n1, n2)

    elif escolha == '*':
        multiplicacao(n1, n2)

    elif escolha == '/':
        divisao(n1, n2)

    else:
        print('Opcao invalida')

calculadora()