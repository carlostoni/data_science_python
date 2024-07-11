# Crie um array de 20 elementos.
# import numpy as np

# array_sequencia = np.arange(20)
# print(array_sequencia)


# Extraia os primeiros 5 elementos, os últimos 5 elementos e os elementos 
# das posições 5 a 10.

# import numpy as np

# array_sequencia = np.arange(20)
# print(f'''Primeiros 5: {array_sequencia[:5]}
# Ultimos 5: {array_sequencia[-5:]}''')

# Utilize uma função para extrair o produto das matrizes de 20 elementos, se necessário 
# crie mais uma. 

import numpy as np

ale1 =np.random.randint(0,20, 20)
ale2 =np.random.randint(0,20, 20)

concatenado = np.concatenate((ale1, ale2))

soma = np.sum(concatenado)

mult =  np.dot(ale1, ale2)

print(f'''Array 1: {ale1}, 
Array 2: {ale2}''')
print(f'''Concatenado: {concatenado}''')
print(f'''Soma: {soma}''')
print(f'''Multiplicacao: {mult}''')




