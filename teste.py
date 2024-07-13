import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('/mnt/data/file-3JdQMvkMlN0Ewu9ubG7osj8X')

# Agrupa os dados por "Spectral Class" e soma os valores de "Star color"
dados_agrupados = dados.groupby('Spectral Class')['Star color'].sum().reset_index()

# Converte as colunas agrupadas em listas
spectral = dados_agrupados['Spectral Class'].tolist()
star_color = dados_agrupados['Star color'].tolist()

# Cria o gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(spectral, star_color)

# Adiciona os valores no topo de cada barra
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Configura o Tkinter
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