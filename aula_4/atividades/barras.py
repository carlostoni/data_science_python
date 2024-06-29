# 3 - Desenvolva em gráfico  barras:
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

medias_jose = [10,5,8,9,10,5,4]
meses = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']

bars = plt.bar(meses, medias_jose)

plt.title('NUMEROS DE VENDAS')
plt.xlabel('MESES')
plt.ylabel('MEDIAS')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom')

plt.ylim(0, 10)
plt.yticks(range(0, 12))  
plt.grid(True, axis='y')

plt.show()