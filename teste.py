import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('/mnt/data/file-3JdQMvkMlN0Ewu9ubG7osj8X')

# Converte a coluna 'Star color' em uma coluna numérica se necessário
# Caso a coluna 'Star color' não seja numérica, será necessário converter ou ajustar a forma como os valores são somados
# Aqui assumimos que a coluna é numérica ou contém valores que podem ser convertidos para numérico
dados['Star color'] = pd.to_numeric(dados['Star color'], errors='coerce').fillna(0)

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


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('brasileirao.csv')


# Converte as colunas de interesse em listas
team = dados['team'].fillna(0).to_list()
points = dados['points'].fillna(0).to_list()

# Seleciona uma porção dos dados para visualização
n_team = team[1:1000]
n_points  = points [1:1000]

# Cria o gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(n_team, n_points)

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


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carrega os dados do arquivo CSV
dados = pd.read_csv('brasileirao.csv')

# Agrupa os dados por time e soma os pontos
soma_pontos_por_time = dados.groupby('team')['points'].sum().reset_index()

# Converte as colunas de interesse em listas
team = soma_pontos_por_time['team'].fillna(0).to_list()
points = soma_pontos_por_time['points'].fillna(0).to_list()

# Seleciona uma porção dos dados para visualização (se necessário)
n_team = team[:50]  # Mostra apenas os primeiros 50 times (ajuste conforme necessário)
n_points = points[:50]

# Cria o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(n_team, n_points, color='skyblue')
ax.set_xlabel('Pontos')
ax.set_ylabel('Time')
ax.set_title('Total de Pontos por Time no Campeonato Brasileiro')

# Adiciona rótulos de valor em cada barra
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