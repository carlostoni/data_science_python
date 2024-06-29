8import matplotlib.pyplot as plt
import seaborn as sns

# Dados salariais
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

# Cálculo da média e desvio padrão
medias = [statistics.mean(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
desvios = [statistics.stdev(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]

# Seleção de gráfico (média ou desvio)
escolha = input("Digite 'media' para média ou 'desvio' para desvio padrão: ")

if escolha == "media":
    # Gráfico de média
    sns.barplot(x=["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], y=medias)
    plt.xlabel("Empresa")
    plt.ylabel("Média Salarial")
    plt.title("Média Salarial por Empresa")
    plt.show()
elif escolha == "desvio":
    # Gráfico de desvio padrão
    sns.barplot(x=["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], y=desvios)
    plt.xlabel("Empresa")
    plt.ylabel("Desvio Padrão")
    plt.title("Desvio Padrão Salarial por Empresa")
    plt.show()
else:
    print("Opção inválida. Digite 'media' ou 'desvio'.")


import matplotlib.pyplot as plt
import statistics

# Dados salariais
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

# Cálculo de medidas estatísticas
medias = [statistics.mean(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
desvios = [statistics.stdev(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]

# Seleção de gráfico (média ou desvio)
escolha = input("Digite 'media' para média ou 'desvio' para desvio padrão: ")

# Criando o gráfico
plt.figure(figsize=(10, 6))

if escolha == "media":
    # Gráfico de média (barras)
    plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], medias, color='skyblue')
    plt.xlabel("Empresa")
    plt.ylabel("Média Salarial")
    plt.title("Média Salarial por Empresa")
elif escolha == "desvio":
    # Gráfico de desvio padrão (linhas)
    plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], desvios, marker='o', linestyle='-', color='lightcoral')
    plt.xlabel("Empresa")
    plt.ylabel("Desvio Padrão")
    plt.title("Desvio Padrão Salarial por Empresa")
else:
    print("Opção inválida. Digite 'media' ou 'desvio'.")

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



Código Completo sem Seaborn (Matplotlib puro)
import matplotlib.pyplot as plt
import statistics

# Dados salariais
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

# Funções para calcular medidas estatísticas
def media(lista):
  """
  Calcula a média aritmética de uma lista.
  """
  return statistics.mean(lista)

def mediana(lista):
  """
  Calcula a mediana de uma lista.
  """
  return statistics.median(lista)

def moda(lista):
  """
  Calcula a moda de uma lista.
  """
  return statistics.mode(lista)

def variancia(lista):
  """
  Calcula a variância de uma lista.
  """
  return statistics.variance(lista)

def desvio(lista):
  """
  Calcula o desvio padrão de uma lista.
  """
  return statistics.stdev(lista)

# Cálculo de medidas estatísticas por empresa
medias = [media(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
medianas = [mediana(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
modas = [moda(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
variancas = [variancia(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
desvios = [desvio(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]

# Seleção de gráfico (média, mediana, moda, variância ou desvio)
escolha = input("Digite a medida que deseja analisar (média, mediana, moda, variância ou desvio): ").lower()

# Validação da escolha
validas = ["média", "mediana", "moda", "variância", "desvio"]
if escolha not in validas:
  print(f"Opção inválida! Escolha uma das medidas disponíveis: {validas}")
  exit()

# Criação do gráfico
plt.figure(figsize=(12, 6))

if escolha == "média":
  # Gráfico de média (barras)
  plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], medias, color='skyblue')
  plt.xlabel("Empresa")
  plt.ylabel("Média Salarial")
  plt.title(f"Média Salarial por Empresa")
elif escolha == "mediana":
  # Gráfico de mediana (barras)
  plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], medianas, color='lightcoral')
  plt.xlabel("Empresa")
  plt.ylabel("Mediana Salarial")
  plt.title(f"Mediana Salarial por Empresa")
elif escolha == "moda":
  # Gráfico de moda (barras)
  plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], modas, color='gold')
  plt.xlabel("Empresa")
  plt.ylabel("Moda Salarial")
  plt.title(f"Moda Salarial por Empresa")
elif escolha == "variância":
  # Gráfico de variância (barras)
  plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], variancias, color='lightgreen')
  plt.xlabel("Empresa")
  plt.ylabel("Variância Salarial")
  plt.title(f"Variância Salarial por Empresa")
elif escolha == "desvio":
  # Gráfico de desvio padrão (barras)
  plt.bar(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], desvios, color='lightblue')
  plt.xlabel("Empresa")
  plt.ylabel("Desvio Padrão


