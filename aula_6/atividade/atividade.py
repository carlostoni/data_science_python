import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dados = pd.read_csv('brasileirao.csv')
#soma_pontos_por_time = dados.groupby('team')['points'].sum().reset_index()

team = dados['team'].fillna(0).to_list()
points = dados['points'].fillna(0).to_list()
posicao = dados['place'].fillna(0).to_list()

n_team = team[0:176]
n_points  = points[0:176]
n_posicao = posicao[0:176]



fig, ax = plt.subplots()
bars = ax.barh(n_team, n_points)
ax.set_xlabel('Pontos')
ax.set_ylabel('Time')
ax.set_title('Total de Pontos por Time no Campeonato Brasileiro')

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

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

janela.mainloop()