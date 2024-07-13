import pandas as pd
import matplotlib.pyplot as plt

# Carregamento dos dados
dados = pd.read_csv('covid_19.csv')

# Preenchimento de valores ausentes
dados['população'].fillna(0, inplace=True)
dados['testes'].fillna(0, inplace=True)

# Seleção de dados
populacao = dados['população'].to_list()
testes = dados['testes'].to_list()

# Geração do gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(dados['continente'], populacao, label='População')
plt.bar(dados['continente'], testes, label='Testes', bottom=populacao)
plt.xlabel('Continente')
plt.ylabel('Quantidade')
plt.title('População e Testes de COVID-19 por Continente')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
