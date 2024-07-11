##2
# Qual é a média dos números [10, 20, 30, 40, 50] usando o módulo statistics?
# from statistics import *

# numeros = [10, 20, 30, 40, 50]

# media  = mean(numeros)
# print('A media é :', media)

##3
#Qual é a mediana dos números [3, 1, 4, 1, 5, 9, 2] usando o módulo statistics?
# import statistics

# numeros = [3, 1, 4, 1, 5, 9, 2]

# resultado = statistics.median(numeros)
# print('A mediana é: ', resultado)

##4
#Qual é a moda dos números [6, 1, 6, 7, 9, 6, 4] usando o módulo statistics?
# from statistics import mode

# numeros = [6, 1, 6, 7, 9, 6, 4]

# moda = mode(numeros)
# print(f"Moda: {moda}")

##5
# import numpy as np 

# media = np.mean([4, 8, 15, 16, 23, 42])  
# print(media)

# import numpy as np 
# mediana = np.median([7, 5, 3, 1, 9, 11, 13]) 
# print(mediana)


# DESAFIO MATPLOT LIB, PANDAS, NUMPY
# Neste desafio, você irá criar um sistema que lê dados de um arquivo CSV, processa esses dados usando NumPy e Pandas, e gera gráficos com Matplotlib. 
# Siga o passo a passo abaixo para completar a tarefa.


# Passo 1: Instalação das Bibliotecas
# Antes de começar, você precisa instalar as bibliotecas necessárias. Abra o terminal ou prompt de comando e execute os seguintes comandos:

# Passo 2: Preparação dos Dados
# Crie um arquivo CSV chamado dados.csv com o seguinte conteúdo:

# Passo 3: Criação do Sistema
# Agora, vamos criar o script Python que realizará as seguintes tarefas:
# Ler o arquivo CSV usando Pandas.
# Processar os dados usando NumPy.
# Gerar gráficos usando Matplotlib.
# Exibir a interface gráfica com Tkinter.
# Crie 5 botões 
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também

import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *




def selecionar():
    Tk().withdraw()
    caminho = askopenfilename(
    filetypes = (("Arquivo CSV","*.csv"),),
    title = "SELECIONAR ARQUIVO CSV"

   

    )
    return caminho

def data_plot():
    caminho = selecionar()

    if caminho:
     dados = pd.read_csv(caminho)
     vendas = dados['vendas'].to_list()
     vendedor = dados['vendedor'].to_list()

     fig,grafico = plt.subplots()
     grafico.plot(vendedor, vendas)
     
     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

     

    else:
        print('erro')

    
def data_bar():
    caminho = selecionar()

    if caminho:
     dados = pd.read_csv(caminho)
     vendas = dados['vendas'].to_list()
     vendedor = dados['vendedor'].to_list()

     fig,grafico = plt.subplots()
     grafico.bar(vendedor, vendas)
     
     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    else:
        print('erro')
def data_pie():
    caminho = selecionar()

    if caminho:
     plt.style.use('_mpl-gallery-nogrid')

     dados = pd.read_csv(caminho)
     colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(dados)))
     vendas = dados['vendas'].to_list()
     vendedor = dados['vendedor'].to_list()
          
     fig, grafico = plt.subplots()
     grafico.pie(vendas,labels=vendedor, colors=colors)
            
     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def data_scatter():
    caminho = selecionar()

    if caminho:
     dados = pd.read_csv(caminho)
     vendas = dados['vendas'].to_list()
     vendedor = dados['vendedor'].to_list()

     fig,grafico = plt.subplots()
     grafico.scatter(vendedor, vendas)
     
     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def data_stem():
    caminho = selecionar()

    if caminho:
     dados = pd.read_csv(caminho)
     vendas = dados['vendas'].to_list()
     vendedor = dados['vendedor'].to_list()

     fig,grafico = plt.subplots()
     
     grafico.stem(vendedor,vendas)
     
     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
   
     
    

    else:
        print('erro')


janela = tk.Tk()
janela.geometry("1920x1080")

btn1 = tk.Button(janela, text='Plot ', command=data_plot)
btn1.pack(pady=5)

btn2 = tk.Button(janela, text='Bar', command=data_bar)
btn2.pack(pady=5)

btn3 = tk.Button(janela, text='Pie', command=data_pie)
btn3.pack(pady=5)

btn4 = tk.Button(janela, text='Scatter', command=data_scatter)
btn4.pack(pady=5)

btn5 = tk.Button(janela, text='Stem', command=data_stem)
btn5.pack(pady=5)





janela.mainloop()






