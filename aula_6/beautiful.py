import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from bs4 import BeautifulSoup


html= """


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    <h1>teste</h1>
    <p: class="paragrafo">Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
      Quod accusantium iusto, enim earum autem ipsam at cumque asperiores distinctio repudiandae quia ex suscipit? 
      Est nobis quae, eum recusandae qui necessitatibus!</p>

    <header>
      <table>
        <thead class=" colunas">
          <tr>
            <th>linha 1</th>
            <th>linha 2</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>dado1</td>
            <td>dado2</td>
          </tr>

        </tbody>

      </table>
    </header>

</body>
</html>


"""

soup = BeautifulSoup(html, 'html.parser')
titulo = soup.find('h1').get_text()
lista = []
lista.append(titulo)
print(lista)

print(titulo)
text = soup.find_all('thead', 'colunas')
t2 = soup.find_all('tr')
print(text)