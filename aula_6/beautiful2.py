import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from bs4 import BeautifulSoup
import requests

url = 'https://tabelatest.netlify.app/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

n = soup.find('tbody').get_text().replace('\n',' ' )
n2 = soup.find('tr').get_text().replace('\n', ' ')
lista = []
lista.append(n2)
lista.append(n)
print(lista)








