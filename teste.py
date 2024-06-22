class AlunosNotas:
    def __init__(self):
        self.alunos = [
            {'matematica': [1, 2, 3], 'portugues': [7, 2, 3], 'quimica': [1, 2, 3]},
            {'matematica': [1, 2, 3], 'portugues': [7, 2, 3], 'quimica': [1, 2, 3]},
            {'matematica': [1, 2, 3], 'portugues': [7, 2, 3], 'quimica': [1, 2, 3]},
            {'matematica': [1, 2, 3], 'portugues': [7, 2, 3], 'quimica': [1, 2, 3]},
            {'matematica': [1, 2, 3], 'portugues': [7, 2, 3], 'quimica': [1, 2, 3]}
        ]

    def get_aluno_dados(self, aluno_num):
        if 1 <= aluno_num <= len(self.alunos):
            return self.alunos[aluno_num - 1]
        else:
            return None


def main():
    alunos = AlunosNotas()
    escolha_aluno = int(input('Escolha o aluno (1-5): '))
    dados = alunos.get_aluno_dados(escolha_aluno)

    if dados is None:
        print('Aluno inválido')
        return

    escolha = input('''
1- Moda
2- Media
3- Mediana
4- Desvio
5- Varianca
6- Amplitude
7- Todos
''')

    materias = ['matematica', 'portugues', 'quimica']

    if escolha == '1':
        for materia in materias:
            print(f"Moda de {materia}: {moda(dados[materia])}")
    elif escolha == '2':
        for materia in materias:
            print(f"Média de {materia}: {media(dados[materia])}")
    elif escolha == '3':
        for materia in materias:
            print(f"Mediana de {materia}: {mediana(dados[materia])}")
    elif escolha == '4':
        for materia in materias:
            print(f"Desvio padrão de {materia}: {desvio(dados[materia])}")
    elif escolha == '5':
        for materia in materias:
            print(f"Variância de {materia}: {var(dados[materia])}")
    elif escolha == '6':
        for materia in materias:
            print(f"Amplitude de {materia}: {amplitude(dados[materia])}")
    elif escolha == '7':
        for materia in materias:
            print(f"Moda de {materia}: {moda(dados[materia])}")
            print(f"Média de {materia}: {media(dados[materia])}")
            print(f"Mediana de {materia}: {mediana(dados[materia])}")
            print(f"Desvio padrão de {materia}: {desvio(dados[materia])}")
            print(f"Variância de {materia}: {var(dados[materia])}")
            print(f"Amplitude de {materia}: {amplitude(dados[materia])}")
    else:
        print('Opção inválida')

if __name__ == '__main__':
    main()
