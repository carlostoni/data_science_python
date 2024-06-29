import matplotlib.pyplot as plt
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
