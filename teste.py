import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('/mnt/data/file-3JdQMvkMlN0Ewu9ubG7osj8X')

# Converte as colunas de interesse em listas
spectral = dados['Spectral Class'].fillna(0).to_list()
star_color = dados['Star color'].fillna(0).to_list()

# Seleciona uma porção dos dados para visualização
n_spectral = spectral[1:176]
n_star_color = star_color[1:176]

# Cria o gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(n_spectral, n_star_color)

# Adiciona os valores no topo de cada barra
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Configura o Tkinter
Tk().withdraw()
janela = tk.Tk()
janela.geometry("1920x1080")

# Adiciona o gráfico ao canvas
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Inicia o loop principal do Tkinter
janela.mainloop()