# Desafio 1: Integração de Entrada de Dados
# Modifique o código para permitir que o usuário entre com dados de vendas para diferentes meses e plote o gráfico com base nesses dados:

# Atualize a função criar_grafico() para ler os dados dessas caixas de entrada e plotar o gráfico com base nesses dados.
# Garanta que os dados inseridos sejam válidos (por exemplo, números inteiros ou flutuantes).

import statistics
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib.figure import Figure

def calcular_estatisticas(lista):
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
        try:
            empresa5 = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get())]
        except ValueError:
            messagebox.showerror('Erro', 'Por favor, insira apenas números nos campos de entrada.')
            return
        dado = empresa5
    else:
        messagebox.showerror('Erro', 'Esse dado não existe.')
        return

    media, moda, mediana, desvio, varianca = calcular_estatisticas(dado)

    resultado_text = (f'''
    Média: {media}
    Moda: {moda}
    Mediana: {mediana}
    Desvio Padrão: {desvio}
    Variância: {varianca}
    ''')

    resultado_label.config(text=resultado_text)

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title(f'Cargos e Salários - {empresa_selecionada}')
    ax.set_xlabel('Cargos')
    ax.set_ylabel('Salários')
    cargos = ['Estágio', 'Vendedor', 'Supervisor', 'Gestor', 'CEO']
    ax.plot(cargos, dado, marker='o')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT)

def atualizar_entradas(event):
    if empresa_var.get() == 'Empresa 5':
        entry1.config(state='normal')
        entry2.config(state='normal')
        entry3.config(state='normal')
        entry4.config(state='normal')
        entry5.config(state='normal')
    else:
        entry1.config(state='disabled')
        entry2.config(state='disabled')
        entry3.config(state='disabled')
        entry4.config(state='disabled')
        entry5.config(state='disabled')

root = tk.Tk()
root.title('Cargos e Salários')

empresa_var = tk.StringVar(value='Empresa 1')
empresa_opcoes = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4', 'Empresa 5']
menu = ttk.Combobox(root, textvariable=empresa_var, values=empresa_opcoes)
menu.pack()
menu.bind("<<ComboboxSelected>>", atualizar_entradas)

tk.Label(root, text='Empresa 5 - Entrada de Números:').pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
entry3 = tk.Entry(root)
entry3.pack()
entry4 = tk.Entry(root)
entry4.pack()
entry5 = tk.Entry(root)
entry5.pack()


atualizar_entradas(None)

btn = tk.Button(root, text='Analisar', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT)

root.mainloop()

