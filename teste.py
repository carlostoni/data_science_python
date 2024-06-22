import matplotlib.pyplot as plt

from  media import media1
from matplotlib import pyplot as plt

aluno1 = [4,5,7]
aluno1.sort()

aluno2 = [5,3,8]
aluno2.sort()

aluno3 = [5,5,5]
aluno3.sort()

aluno4 = [1,2,4]
aluno4.sort()


cargos = ["Reprovado","Recupercao","Aprovado"]

def hadle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)

hadle(aluno1, aluno1)  
hadle(aluno2, aluno2)   
hadle(aluno3, aluno3) 
hadle(aluno4, aluno4) 

plt.title('CARGOS, SALARIOS')
plt.ylabel('SALARIOS')
plt.xlabel('CARGOS')

plt.plot(cargos,aluno1, linestyle='--', marker = 'o')
plt.plot(cargos,aluno2, linestyle='--', marker = 'o')
plt.plot(cargos,aluno3, linestyle='--', marker = 'o')
plt.plot(cargos,aluno4, linestyle='--', marker = 'o')
plt.grid(True)

plt.show()


import matplotlib.pyplot as plt

# Função para calcular a média
def media1(lista):
    return sum(lista) / len(lista)

# Notas dos alunos
aluno1 = [4,5,7]
aluno2 = [5,3,8]
aluno3 = [5,5,5]
aluno4 = [1,2,4]

# Ordenar as listas
aluno1.sort()
aluno2.sort()
aluno3.sort()
aluno4.sort()

# Cargos (ou situações)
cargos = ["Reprovado", "Recuperacao", "Aprovado"]

# Calculando as médias
media_aluno1 = media1(aluno1)
media_aluno2 = media1(aluno2)
media_aluno3 = media1(aluno3)
media_aluno4 = media1(aluno4)

# Função para manipular os dados
def hadle(lista, salarios):
    print('EMPRESA', salarios)
    print('----------------------------')
    print('Média:', media1(lista))

# Exibindo médias no console
hadle(aluno1, aluno1)  
hadle(aluno2, aluno2)   
hadle(aluno3, aluno3) 
hadle(aluno4, aluno4) 

# Configuração do gráfico
plt.title('CARGOS, SALARIOS')
plt.ylabel('SALARIOS')
plt.xlabel('CARGOS')

# Plotando as notas dos alunos
plt.plot(cargos, aluno1, linestyle='--', marker='o', label=f'Aluno 1 (Média: {media_aluno1:.2f})')
plt.plot(cargos, aluno2, linestyle='--', marker='o', label=f'Aluno 2 (Média: {media_aluno2:.2f})')
plt.plot(cargos, aluno3, linestyle='--', marker='o', label=f'Aluno 3 (Média: {media_aluno3:.2f})')
plt.plot(cargos, aluno4, linestyle='--', marker='o', label=f'Aluno 4 (Média: {media_aluno4:.2f})')

# Adicionando as médias ao gráfico como texto
plt.text(2, aluno1[-1], f'{media_aluno1:.2f}', ha='center', va='bottom')
plt.text(2, aluno2[-1], f'{media_aluno2:.2f}', ha='center', va='bottom')
plt.text(2, aluno3[-1], f'{media_aluno3:.2f}', ha='center', va='bottom')
plt.text(2, aluno4[-1], f'{media_aluno4:.2f}', ha='center', va='bottom')

# Adicionando a legenda
plt.legend()

# Exibindo a grade
plt.grid(True)

# Exibindo o gráfico
plt.show()


import matplotlib.pyplot as plt

# Função para calcular a média
def media1(lista):
    return sum(lista) / len(lista)

# Notas dos alunos
aluno1 = [4, 5, 7]
aluno2 = [5, 3, 8]
aluno3 = [5, 5, 5]
aluno4 = [1, 2, 4]

# Ordenar as listas
aluno1.sort()
aluno2.sort()
aluno3.sort()
aluno4.sort()

# Cargos (ou situações)
cargos = ["Reprovado", "Recuperacao", "Aprovado"]

# Calculando as médias
media_aluno1 = media1(aluno1)
media_aluno2 = media1(aluno2)
media_aluno3 = media1(aluno3)
media_aluno4 = media1(aluno4)

# Função para manipular os dados
def hadle(lista, salarios):
    print('EMPRESA', salarios)
    print('----------------------------')
    print('Média:', media1(lista))

# Exibindo médias no console
hadle(aluno1, aluno1)  
hadle(aluno2, aluno2)   
hadle(aluno3, aluno3) 
hadle(aluno4, aluno4) 

# Configuração do gráfico
plt.title('Médias dos Alunos')
plt.ylabel('Média')
plt.xlabel('Alunos')

# Dados para o gráfico de barras
alunos = ['Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4']
medias = [media_aluno1, media_aluno2, media_aluno3, media_aluno4]

# Plotando o gráfico de barras
bars = plt.bar(alunos, medias, color=['blue', 'orange', 'green', 'red'])

# Adicionando as médias ao topo das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom')

# Exibindo a grade
plt.grid(True, axis='y')

# Exibindo o gráfico
plt.show()