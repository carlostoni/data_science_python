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

# Ajustando a grade e o limite do eixo y
plt.ylim(0, 10)
plt.yticks(range(0, 11))  # Ticks de 0 a 10

# Exibindo a grade
plt.grid(True, axis='y')

# Exibindo o gráfico
plt.show()