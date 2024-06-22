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

# main.py

from dados import ensino_medio, ensino_fundamental, alunos
import estatisticas as est

def calcular_estatisticas_por_aluno(dados_aluno):
    estatisticas = {}
    estatisticas['media'] = est.calcular_media(dados_aluno)
    estatisticas['variancia'] = est.calcular_variancia(dados_aluno)
    estatisticas['amplitude'] = est.calcular_amplitude(dados_aluno)
    estatisticas['desvio_padrao'] = est.calcular_desvio_padrao(dados_aluno)
    estatisticas['mediana'] = est.calcular_mediana(dados_aluno)
    estatisticas['moda'] = est.calcular_moda(dados_aluno)
    return estatisticas

def mostrar_estatisticas(estatisticas, descricao):
    print(f"\nEstatísticas para {descricao}:")
    for chave, valor in estatisticas.items():
        print(f"{chave.capitalize()}: {valor}")

if __name__ == "__main__":
    # Calculando estatísticas para ensino médio
    estatisticas_em = {
        'media': est.calcular_media(ensino_medio),
        'variancia': est.calcular_variancia(ensino_medio),
        'amplitude': est.calcular_amplitude(ensino_medio),
        'desvio_padrao': est.calcular_desvio_padrao(ensino_medio),
        'mediana': est.calcular_mediana(ensino_medio),
        'moda': est.calcular_moda(ensino_medio)
    }
    mostrar_estatisticas(estatisticas_em, "Ensino Médio")

    # Calculando estatísticas para ensino fundamental
    estatisticas_ef = {
        'media': est.calcular_media(ensino_fundamental),
        'variancia': est.calcular_variancia(ensino_fundamental),
        'amplitude': est.calcular_amplitude(ensino_fundamental),
        'desvio_padrao': est.calcular_desvio_padrao(ensino_fundamental),
        'mediana': est.calcular_mediana(ensino_fundamental),
        'moda': est.calcular_moda(ensino_fundamental)
    }
    mostrar_estatisticas(estatisticas_ef, "Ensino Fundamental")

    # Calculando estatísticas por aluno
    for aluno, notas in alunos.items():
        print(f"\nEstatísticas para {aluno}:")
        notas_lista = list(notas.values())
        estatisticas_aluno = calcular_estatisticas_por_aluno(notas_lista)
        mostrar_estatisticas(estatisticas_aluno, aluno)

    input('clique enter para sair')