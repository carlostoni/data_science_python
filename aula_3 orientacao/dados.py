class Dados:
    def __init__(self):
        self.dados = {}
        self.inserir_dados_inicial()

    def inserir_dados_inicial(self):
        self.dados['empresa1'] = [1000, 6000, 1200, 8000, 1400]
        self.dados['empresa2'] = [5000, 4000, 3000, 2000, 7000]
        self.dados['empresa3'] = [1200, 1300, 8000, 3000, 15000]
        self.dados['empresa4'] = [1400, 1750, 2000, 4500, 5900, 7000]
        self.dados['empresa5'] = [1400, 1750, 2000, 4500, 5900, 7000]

    def adicionar_dado(self, empresa, dado):
        if empresa in self.dados:
            self.dados[empresa].append(dado)
        else:
            self.dados[empresa] = [dado]

    def obter_dados(self):
        return self.dados


class Resolucao:
    def __init__(self):
        self.dados = Dados().obter_dados()

    def mostrar_dados(self):
        for empresa, valores in self.dados.items():
            print(f"{empresa} = {valores}")

# Programa principal
if __name__ == "__main__":
    resolucao = Resolucao()
    resolucao.mostrar_dados()