from Moda import moda
from Media import media
from Mediana import mediana
from Desvio import desvio

def main():
    dados = []  
    escolha_range = int(input('Numero de notas: '))
    escolha = input(f'''
1- Moda
2- Media
3- Mediana
4- Desvio
5- Todos
: ''')
    for i in range(escolha_range):
        entrada = input('Insira as notas: ')
        dados.append(int(entrada))
    if escolha == '1':
        moda(dados)
    elif escolha == '2':
        media(dados)
    elif escolha == '3':
        mediana(dados)
    elif escolha == '4':
        desvio(dados) 
    elif escolha == '5':
        moda(dados)
        media(dados)
        mediana(dados)
        desvio(dados) 
    else:
        print('erro')
        

main()