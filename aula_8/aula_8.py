import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('aula_8\dados.xlsx')
sns.barplot(data=df, x='vendas', y ='vendedor')
plt.show()