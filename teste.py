class Dados:
    def __init__(self):
        self.dados = []
        self.inserir_dados_inicial()

    def inserir_dados_inicial(self):
        dados_iniciais = [
            {'id': 1, 'nome': 'Carlos', 'idade': 25},
            {'id': 2, 'nome': 'Ana', 'idade': 22},
            {'id': 3, 'nome': 'João', 'idade': 30},
            {'id': 4, 'nome': 'Maria', 'idade': 28},
        ]
        for dado in dados_iniciais:
            self.dados.append(dado)

    def adicionar_dado(self, dado):
        self.dados.append(dado)

    def obter_dados(self):
        return self.dados

# Exemplo de uso
if __name__ == "__main__":
    dados = Dados()
    print(dados.obter_dados())

# dados.py

import random

# Definindo o número de alunos e a faixa de notas para cada matéria
NUM_ALUNOS = 10
MATERIAS = ['materia1', 'materia2', 'materia3']
NOTA_MIN = 0
NOTA_MAX = 10

# Gerando os dados dos alunos
alunos = {}
for i in range(1, NUM_ALUNOS + 1):
    nome_aluno = f'aluno{i}'
    notas = {materia: random.randint(NOTA_MIN, NOTA_MAX) for materia in MATERIAS}
    alunos[nome_aluno] = notas

# Exemplo de dados para ensino médio e fundamental
ensino_medio = list(range(1, 151))
ensino_fundamental = [1, 8, 9, 10, 3, 5, 8, 8, 9]