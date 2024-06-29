import statistics
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib.figure import Figure

def calcular_estatica(lista):
    media = statistics.mean(lista)
    moda = statistics.mode(lista)
    mediana = statistics.median(lista)
    desvio = statistics.stdev(lista)
    varianca = statistics.variance(lista)
    return media, moda, mediana, desvio, varianca

def mostrar_analise():
    empresa1 = [1000, 6000, 1200, 8000, 1400]
    empresa1.sort()
    empresa2 = [5000, 4000, 3000, 2000, 7000]
    empresa2.sort()
    empresa3 = [1200, 1300, 8000, 3000, 15000]
    empresa3.sort()
    empresa4 = [1400, 1750, 2000, 4500, 5900]
    empresa4.sort()

    empresa5 = []  # Insira os dados da Empresa 5 aqui
    empresa5.sort()

    cargos = ['Estagiário', 'Vendedor', 'Supervisor', 'Gestor', 'CEO']

    empresa_selecionada = empresa_var.get()

    if empresa_selecionada == 'Empresa 1':
        dado = empresa1
    elif empresa_selecionada == 'Empresa 2':
        dado = empresa2
    elif empresa_selecionada == 'Empresa 3':
        dado = empresa3
    elif empresa_selecionada == 'Empresa 4':
        dado = empresa4
    elif empresa_selecionada == 'Empresa 5':
        dado = empresa5
    else:
        messagebox.showerror('Erro', 'Esse dado não existe')
        return

    media, moda, mediana, desvio, varianca = calcular_estatica(dado)

    resultado_text = f"""
        MÉDIA: {media}
        MODA: {moda}
        MEDIANA: {mediana}
        DESVIO PADRÃO: {desvio}
        VARIANÇA: {varianca}

        """

    resultado_label.config(text=resultado_text)

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title('Cargos e Salários')
    ax.set_xlabel('Cargos')
    ax.set_ylabel('Salários')
    ax.plot(cargos, dado)
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title('Cargos e Salários')

empresa_var = tk.StringVar(value='Empresa 1')
empresa_opcoes = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4', 'Empresa 5']
menu = ttk.Combobox(root, textvariable=empresa_var, values=empresa_opcoes)
menu.pack()

# Campo de entrada de dados para a Empresa 5
empresa5_entry = tk.Entry(root)
empresa5_entry.pack()

btn = tk.Button(root, text='Analisar', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)

root.mainloop()
