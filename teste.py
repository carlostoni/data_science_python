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
