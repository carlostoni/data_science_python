import statistics
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)


def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)


def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')


def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 



empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900,7000]

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

enter=input('enter para sair')


def grafico():
    #dados
    vendas_em_milhoes = [15,20,30,6,89,15,20]
    meses =['JAN', 'FEV', 'MAR', 'ABR', 'MAIO', 'JUN','JUL']
    cores = ['red', 'blue', 'green', 'purple', 'orange', 'grey', 'yellow']

    #criando grafico
    fig, ax = plt.subplots()

    ax.pie(vendas_em_milhoes,colors=cores, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True, labels = meses)

    #rotulos
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

    #integracao de grafico
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

janela = tk.Tk()
janela.title("VENDAS")

frame_grafico = tk.Frame(janela)
frame_grafico.pack()

btn = tk.Button(janela, text= 'mostrar grafico', command= grafico)
btn.pack()

btn2 = tk.Button(janela, text= 'fechar', command= quit)
btn2.pack()

janela.mainloop()
def quit(self):
        self.root.destroy()
plt.show()


