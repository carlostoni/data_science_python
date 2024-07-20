#Análise de Vendas: Dados de vendas de uma loja, incluindo data, produto, preço, quantidade vendida, etc.

import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


# Conectar ao banco de dados (será criado se não existir)
conexao = sqlite3.connect('aula_8\projeto_final\db.db')
cursor = conexao.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data INTEGER NOT NULL,
        produto TEXT NOT NULL,
        preço INTEGER NOT NULL,
        quantidade INTEGER NOT NULL
        
    )
''')
conexao.commit()




#criar a extrutura que mostrara o banco de dados

def inserir_dados():
    data = entrada_data.get()
    produto = entrada_produto.get()
    preço = entrada_preço.get()
    quantidade = entrada_quantidade.get()


    if data and produto.isdigit() and preço:
        cursor.execute('''
        INSERT INTO vendas (data, produto, preço, quantidade)
        VALUES(?,?,?,?)
        ''', (data, produto, preço, quantidade))

        conexao.commit()
        messagebox.showinfo('showinfo','Dados Inseridos')
        entrada_data.delete(0, tk.END)
        entrada_produto.delete(0, tk.END)
        entrada_preço.delete(0, tk.END)
        entrada_quantidade.delete(0,tk.END)
    else:
        messagebox.showwarning('showwarning', 'Algo deu errado')


# Função para exibir dados em um gráfico
def exibir_grafico():
    cursor.execute('SELECT data, produto FROM vendas')
    dados = cursor.fetchall()
    
    if dados:
        datas = [dado[0] for dado in dados]
        produtos = [dado[1] for dado in dados]

        plt.figure(figsize=(10, 5))
        plt.bar(datas, produtos, color='skyblue')
        plt.xlabel('data')
        plt.ylabel('produto')
        plt.title('produto das vendas')
        plt.show()
    else:
        messagebox.showwarning("Erro", "Nenhum dado encontrado para exibir.")





# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de vendas")

# Rótulos e campos de entrada
tk.Label(janela, text="Data:").grid(row=0, column=0, padx=10, pady=5)
entrada_data = tk.Entry(janela)
entrada_data.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Produto:").grid(row=1, column=0, padx=10, pady=5)
entrada_produto = tk.Entry(janela)
entrada_produto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Preço:").grid(row=2, column=0, padx=10, pady=5)
entrada_preço = tk.Entry(janela)
entrada_preço.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Quantidade:").grid(row=3, column=0, padx=10, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados)
btn_inserir.grid(row=4, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()

# Fechar a conexão ao banco de dados quando a janela for fechada
conexao.close()
