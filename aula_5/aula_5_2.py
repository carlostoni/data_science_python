import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1,6)
x = ['a','b','c','d','e']



plt.bar(x, y)
plt.grid(True)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Linhas')


plt.show()