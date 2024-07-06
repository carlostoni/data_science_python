# ***pib=[150,300,500,800,150,300,900]
# estados=['SP','RS','BA','PE','ES','MT','MS']***

# - ***2 estruture no tkinter um sistema de visualização através do clique, MOSTRE:
# METRICAS
# GRAFICO DE BARRAS***


import statistics
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib.figure import Figure

def mostrar_analise():
    pib=[150,300,500,800,150,300,900]
    estados=['SP','RS','BA','PE','ES','MT','MS']

    pib_selecionada = pib_var.get()
    if pib_selecionada == 'PIB':
        dado = pib
    else:
        messagebox.showerror('Erro', 'Esse dado não existe.')
        return

    #resultado_label.config(text=resultado_text)

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title(f'Cargos e PIB - {pib_selecionada}')
    ax.set_xlabel('Estados')
    ax.set_ylabel('PIB')
    estados=['SP','RS','BA','PE','ES','MT','MS']
    ax.plot(estados, dado, marker='o')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT)

root = tk.Tk()
root.title('Cargos e Salários')

pib_var = tk.StringVar(value='PIB')
pib_opcoes = ['PIB']
menu = ttk.Combobox(root, textvariable=pib_var, values=pib_opcoes)
menu.pack()

btn = tk.Button(root, text='Analisar', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT)

root.mainloop()
