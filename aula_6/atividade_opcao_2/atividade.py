import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('6class.csv')



# Converte as colunas de interesse em listas
spectral = dados['Spectral Class'].fillna(0).to_list()
star_color = dados['Star color'].fillna(0).to_list()

# Seleciona uma porção dos dados para visualização
n_spectral = spectral[1:176]
n_star_color = star_color[1:176]

# Cria o gráfico de barras
fig, ax = plt.subplots()
bars = ax.barh(n_star_color, n_spectral)

for bar in bars:
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width():.0f}', va='center', ha='left')

def on_closing():
    janela.quit()
    janela.destroy()


Tk().withdraw()
janela = tk.Tk()
janela.geometry("1920x1080")
janela.protocol("WM_DELETE_WINDOW", on_closing)

# Adiciona o gráfico ao canvas
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Inicia o loop principal do Tkinter
janela.mainloop()