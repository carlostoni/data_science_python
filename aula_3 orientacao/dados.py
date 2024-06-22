class EmpresaDados:
    def __init__(self):
        self.empresa1 = [1000, 6000, 1200, 8000, 1400]
        self.empresa2 = [5000, 4000, 3000, 2000, 7000]
        self.empresa3 = [1200, 1300, 8000, 3000, 15000]
        self.empresa4 = [1400, 1750, 2000, 4500, 5900, 7000]
        self.empresa5 = [1400, 1750, 2000, 4500, 5900, 7000]

    def get_empresa_dados(self, empresa_num):
        if empresa_num == 1:
            return self.empresa1
        elif empresa_num == 2:
            return self.empresa2
        elif empresa_num == 3:
            return self.empresa3
        elif empresa_num == 4:
            return self.empresa4
        elif empresa_num == 5:
            return self.empresa5
        else:
            return None


from Moda import moda
from Media import media
from Mediana import mediana
from Desvio import desvio

def main():
    empresas = EmpresaDados()  # Cria uma instância da classe EmpresaDados
    escolha_empresa = int(input('Escolha a empresa (1-5): '))
    dados = empresas.get_empresa_dados(escolha_empresa)  # Obtém os dados da empresa selecionada

    if dados is None:
        print('Empresa inválida')
        return

    escolha = input(f'''
1- Moda
2- Media
3- Mediana
4- Desvio
5- Todos
: ''')

    if escolha == '1':
        print('Moda:', moda(dados))
    elif escolha == '2':
        print('Média:', media(dados))
    elif escolha == '3':
        print('Mediana:', mediana(dados))
    elif escolha == '4':
        print('Desvio padrão:', desvio(dados))
    elif escolha == '5':
        print('Moda:', moda(dados))
        print('Média:', media(dados))
        print('Mediana:', mediana(dados))
        print('Desvio padrão:', desvio(dados))
    else:
        print('Opção inválida')

if __name__ == "__main__":
    main()