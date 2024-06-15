from Moda import moda
from Media import media
from Mediana import mediana
from Desvio import desvio
from Dados import empresas

def main(self, listas):
    dados = []  
    escolha_range = int(input('Numero de notas: '))

    self.lists =[ listas.empresa1]
    print(self.lists)




    for i in range(escolha_range):
        entrada = input('Insira as notas: ')
        dados.append(int(entrada))
    
        moda(dados)
        media(dados)
        mediana(dados)
        desvio(dados) 
    
        

main()

