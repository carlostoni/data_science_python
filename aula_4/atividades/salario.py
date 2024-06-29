import statistics
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)
    
    plt.axhline(y= moda, color= 'green', linestyle='-', label = 'Moda' )

def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)

   # plt.axhline(y= mediana, color= 'green', linestyle='-', label = 'Mediana' )

def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

    #plt.axhline(y= varianca, color= 'green', linestyle='-', label = 'Varianca' )

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')

    #plt.axhline(y= desvio, color= 'blue', linestyle='-', label = 'Desvio' )

def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)

    plt.plot(y= media, color= 'red', linestyle='-', label = 'Media' )


 
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

cargos = ["Estagio","Junior","Pleno","Senior","Gerente"]

def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)

handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

plt.title('CARGOS, SALARIOS')
plt.ylabel('SALARIOS')
plt.xlabel('CARGOS')





plt.plot(cargos,empresa1, linestyle='--', marker = 'o')
plt.plot(cargos,empresa2, linestyle='--', marker = 'o')
plt.plot(cargos,empresa3, linestyle='--', marker = 'o')
plt.plot(cargos,empresa4, linestyle='--', marker = 'o')
plt.grid(True)

plt.show()

enter=input('enter para sair')

