import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
     meses = dados['meses'].to_list()
     valores = dados['valores'].to_list()

     fig,grafico = plt.subplots()
     grafico.plot(meses, valores)
     


     canvas = FigureCanvasTkAgg(fig,master=janela)
     canvas.draw()
     canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    else:
        print('erro')



janela = tk.Tk()


btn1 = tk.Button(janela, text='Plot bar', command=data_plot)
btn1.pack(pady=5)
btn2 = tk.Button(janela, text='Fechar', command=janela.destroy)
btn2.pack(pady=5)




janela.mainloop()













# dicionario = {
#     'a': [1,2,3],
#     'b': [4,5,6]
# }

# d1 =[[1,2,3],[3,4,5],[4,436,6],[1,2,3],[3,4,5],[4,436,6]]
# #d2= [3,4,5]



# dados = pd.DataFrame(d1, columns=['a','b','c'])
# dadoss = pd.DataFrame(dicionario)


# print(dadoss.head())
# print(dadoss.tail())
# print(dadoss.describe())


# d = dados['c'][0]
# print(dicionario)