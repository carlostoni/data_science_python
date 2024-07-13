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

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://tabelatest.netlify.app/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the headers
headers = [header.get_text() for header in soup.find_all('th')]

# Extract the rows of the table
rows = []
for row in soup.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    cols = [col.get_text() for col in cols]
    rows.append(cols)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Print the DataFrame
print(df)






