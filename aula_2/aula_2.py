# teste = int(input("digite algo "))
# print("teste")
# print(teste)

# lista0 = []
# lista0 = [1,2,3]
# lista0.append(int(input()))

# print(lista0)
# print(lista0[0])

# tupla = ()
# tupla1 = (1,2,3)
# tupla2 = (1.2,5.2)
# tupla3 = ('a','b')
# tupla4 = (True, False)

# print(tupla1[-1])


# conjunto = {1,3,6,6}

# condicionais
# loops
# while
# funcoes

## lista vetores

# lista0 = [1,2,3]
# lista0.append(int(input()))
# soma = sum(lista0)
# maior = max(lista0)
# menor = min(lista0)
# n1 = 10
# n2 = 20
# n3 = 21
# lista0.extend((n1,n2,n3))
# indice = lista0.index(3)
# lista0.sort()

# print(lista0)
# print('soma',soma)
# print('maior', maior)
# print('menor', menor)
# print('indice', indice)
# print('ordem', lista0 )

# vetor = [[10,2,3],[4,5,6],[21,22,23]]
# print('vetor',vetor[2][2])

# vetor[0]= [150,2]
# print(vetor)
# lista_nova = list(range(0,2000))
# lista_nova2 = list(range(0,2000,5))
# print(lista_nova2)

##condicionais
# n1 = 10
# n2 = 2
# if n1 > n2:
#     print('10 e maior')
# else:
#     print('10 e menor')

# cidade = input('digite sua cidade')
# aeroporto = input('digite o seu aeroporto')

# if cidade == 'sao paulo' or cidade == 'São Paulo'  and  aeroporto == 'guarulhos':
#     print('embarque no sl 10')
# else:
#     print('Embarque no tl 10')

# numero_1 = int(input('Digite um numero: '))
# numero_2 = int(input('Digite outro numero: '))

# if numero_1 % numero_2 ==0:
#     print('e divisivel')
# else:
#     print(' nao e divisivel')


i = 0
while i < 1:
    numero_1 = int(input('Digite um numero: '))
    numero_2 = int(input('Digite outro numero: '))
    operacao = input('digite a operacao: ')


    if operacao == '+':
        soma = numero_1 + numero_2
        print(f'{numero_1} + {numero_2} = ',soma)
        i += 1

    elif operacao == '-':
        subtracao = numero_1 - numero_2
        print(subtracao)

    elif operacao == '*':
        multiplicacao = numero_1 * numero_2
        print(multiplicacao)

    elif operacao == '/':
        divisao = numero_1 / numero_2
        print(divisao)

    else:
        print(' operacao invalida')
print(i)
i += 1



