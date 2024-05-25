# lista = [1,6,6,9,6,69]
# dado = int(input('>> '))
# lista.append(dado)
# if dado > 10:
#     print(f'''o dado inserido r , {dado} na lista
#     {lista}, e maior que 10''')
# elif dado < 10:
#     print(f'''o dado inserido r , {dado} na lista
#     {lista}, e nenor que 10''')
# else:
#     print('digite um numero... ')

import random

aleatorio = random.randint(1,10)
chute = int(input('Digite um numero>> '))

if aleatorio == chute:
    print('acertou', aleatorio)
else:
        print('errou', aleatorio)