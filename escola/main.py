import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

def media1(lista):
    return sum(lista) / len(lista)

aluno1 = [4,5,7]
aluno1.sort()

aluno2 = [5,9,8]
aluno2.sort()

aluno3 = [5,5,5]
aluno3.sort()

aluno4 = [1,2,4]
aluno4.sort()


cargos = ["Reprovado","Recupercao","Aprovado"]

media_aluno1 = media1(aluno1)
media_aluno2 = media1(aluno2)
media_aluno3 = media1(aluno3)
media_aluno4 = media1(aluno4)

def hadle(lista, salarios):

    print('Alunos', salarios)
    print('----------------------------')
    media1(lista)

hadle(aluno1, aluno1)  
hadle(aluno2, aluno2)   
hadle(aluno3, aluno3) 
hadle(aluno4, aluno4) 

plt.title('Médias dos Alunos')

plt.xlabel('Alunos')

x = [0, 1, 2, 3]
y = [2, 3, 5, 10]

# Cria o gráfico
plt.plot(x, y)

# Adiciona rótulos personalizados em três posições
plt.text(-0.5, 2, 'Reprovado', va='center', rotation='vertical')
plt.text(-0.5, 5, 'Recupercao', va='center', rotation='vertical')
plt.text(-0.5, 8, 'Aprovado', va='center', rotation='vertical')



alunos = ['Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4']
medias = [media_aluno1, media_aluno2, media_aluno3, media_aluno4]

bars = plt.bar(alunos, medias)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom')

plt.ylim(0, 10)
plt.yticks(range(0, 10))  

plt.grid(True, axis='y')

plt.show()


