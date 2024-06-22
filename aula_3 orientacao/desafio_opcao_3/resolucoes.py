import sys
from Moda import moda
from Media import media
from Mediana import mediana
from Desvio import desvio
from Varianca import varianca
from Amplitude import amplitude
from alunos import AlunosNotas

for i in range(10):
    def main():
        alunos = AlunosNotas()  
        escolha_aluno = int(input('Escolha o aluno (1-5): '))
        dados = alunos.get_aluno_dados(escolha_aluno)  

        if dados is None:
            print('Aluno inválido')
            return

        escolha = input(f'''
    1- Moda
    2- Media
    3- Mediana
    4- Desvio
    5- Varinca
    6- Amplitude                                      
    7- Todos
    8- Sair
    : ''')
        materias = ['matematica', 'portugues', 'quimica']

        if escolha == '1':
            for materia in materias:
                print(f"Moda em {materia}: {moda(dados[materia])}")
        elif escolha == '2':
            for materia in materias:
                print(f"media em {materia}: {media(dados[materia])}")
        elif escolha == '3':
            for materia in materias:
                print(f"Mediana em {materia}: {mediana(dados[materia])}")
        elif escolha == '4':
            for materia in materias:
                print(f"O Desvio de {materia}: {desvio(dados[materia])} ")
        elif escolha == '5':
            for materia in materias:
                print(f"A Variança em {materia}: {varianca(dados[materia])} ")         
        elif escolha == '6':
            for materia in materias:
                print(f"A Amplitude em {materia}: {amplitude(dados[materia])}")
        elif escolha == '7':
            for materia in materias:
                print(f"Moda em {materia}: {moda(dados[materia])}")
                print(f"Media em {materia}: {media(dados[materia])}")
                print(f"Mediana em {materia}: {mediana(dados[materia])}")
                print(f"O Desvio de {materia}: {desvio(dados[materia])}")
                print(f"A Variança em {materia}: {varianca(dados[materia])}")
                print(f"A Amplitude em {materia}: {amplitude(dados[materia])}")
                print('')
        elif escolha == '8':
                sys.exit()
        else:
            print('Opção inválida')

    if __name__ == "__main__":
        main()