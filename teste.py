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