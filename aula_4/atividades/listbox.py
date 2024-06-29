import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

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
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

janela = tk.Tk()
janela.title("VENDAS")

listbox = tk.Listbox()
items = tk.StringVar()
items.set(
    "Python "
    "C "
    "C++ "
    "Java "
)
listbox = tk.Listbox(listvariable=items)
listbox.pack()


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


