import sqlite3

conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               cidade TEXT NOT NULL
               )
''')
nome = 'Paula'
idade = '30'
cidade = 'São Paulo'
cursor.execute('''
INSERT INTO pessoas(nome, idade, cidade)
               VALUES (?,?,?)
''', (nome, idade, cidade))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f''' ID:{pessoa[0]}, Nome: {pessoa[1]}, idade: {pessoa[2]}, {pessoa[3]}''')
    conexao.close()
