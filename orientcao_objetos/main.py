from Soma import soma
from Subtracao import subtracao
from Multiplicacao import multiplicacao
from Divisao import divisao



def main():
    escolha  = input('(+) (-) (*) (/)')
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    if escolha == '+':
       soma(n1, n2)
       resultado = soma(n1, n2)
       print(resultado)

    elif escolha == '-':
        subtracao(n1, n2)
        resultado = subtracao(n1, n2)
        print(resultado)

    elif escolha == '*':
        multiplicacao(n1, n2)
        resultado = multiplicacao(n1, n2)
        print(resultado)

    elif escolha == '/':
        divisao(n1, n2)
        resultado = divisao(n1, n2)
        print(resultado)
 
    else:
        print('Opcao invalida')

main()