import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## EXEMPLO
# lista = [1,2,3]

# serie = pd.Series(lista)

# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

# est = np.random.randint(1,20,(2,10,3))

# print(f'df ={df}')
# print(f'serie = {serie[0]}')
# print(f'random = {est}')
##

# dados = pd.read_csv('aula_6\covid_19.csv')

# continente = dados['continent'].fillna('outros').to_list()
# falecidos = dados['Deaths'].fillna(0).to_list()

# n_continentes = continente[0:15]
# n_falecidos = falecidos[0:15]


# print(n_continentes)

# print(n_falecidos)

# plt.title("estimativas")
# plt.bar(n_continentes, n_falecidos)
# plt.show()



dados = pd.read_csv('aula_6\covid_19.csv')

populacao = dados['country'].fillna('outros').to_list()
testes = dados['Cases'].fillna(0).to_list()

n_populacao = populacao[1:176]
n_testes = testes[1:176]

print(populacao)
print(testes)



plt.title("estimativas")
plt.bar(n_populacao, n_testes)
plt.show()