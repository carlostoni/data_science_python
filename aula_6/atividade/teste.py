import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('brasileirao.csv')

# Agrupa os dados por time e soma os pontos
#soma_pontos_por_time = dados.groupby('team')['points'].sum().reset_index()

# Converte as colunas de interesse em listas
team = dados['team'].fillna(0).to_list()
points = dados['points'].fillna(0).to_list()
posicao = dados['place'].fillna(0).to_list()
ano = dados['season'].fillna(0).to_list()

# Seleciona uma porção dos dados para visualização (se necessário)
n_team = team[0:176]  # Mostra apenas os primeiros 50 times (ajuste conforme necessário)
n_points = points[0:176]
n_posicao = posicao[0:176]
n_ano = ano[0:176]

# Cria o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(n_team, n_points)
ax.set_xlabel('Pontos')
ax.set_ylabel('Time')
ax.set_title('Total de Pontos por Time no Campeonato Brasileiro')

# Adiciona rótulos de valor em cada barra
for bar, team_posicao in zip(bars, n_posicao):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
            f'{team_posicao}= {bar.get_width():.0f}', va='center', ha='left')

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