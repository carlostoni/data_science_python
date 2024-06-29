import matplotlib.pyplot as plt
import statistics

# Dados salariais
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

# Funções para calcular medidas estatísticas
def media(lista):
  return statistics.mean(lista)

def mediana(lista):
 
  return statistics.median(lista)

def moda(lista):
 
  return statistics.mode(lista)

def variancia(lista):
 
  return statistics.variance(lista)

def desvio(lista):
 
  return statistics.stdev(lista)


medias = [media(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
medianas = [mediana(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
modas = [moda(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
variancas = [variancia(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]
desvios = [desvio(empresa) for empresa in [empresa1, empresa2, empresa3, empresa4]]


escolha = input("Digite a medida que deseja analisar (1= média, 2= mediana, 3= moda, 4= variância ou 5= desvio): ").lower()


plt.figure(figsize=(12, 6))

if escolha == "1":
  
  plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], medias, color='blue')
  plt.xlabel("Empresa")
  plt.ylabel("Média Salarial")
  plt.title(f"Média Salarial por Empresa")
elif escolha == "2":

  plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], medianas, color='blue')
  plt.xlabel("Empresa")
  plt.ylabel("Mediana Salarial")
  plt.title(f"Mediana Salarial por Empresa")
elif escolha == "3":

  plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], modas, color='blue')
  plt.xlabel("Empresa")
  plt.ylabel("Moda Salarial")
  plt.title(f"Moda Salarial por Empresa")
elif escolha == "4":
 
  plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], variancas, color='blue')
  plt.xlabel("Empresa")
  plt.ylabel("Variância Salarial")
  plt.title(f"Variância Salarial por Empresa")
elif escolha == "5":

  plt.plot(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4"], desvios, color='lightblue')
  plt.xlabel("Empresa")
  plt.ylabel("Desvio Padrão")

plt.show()