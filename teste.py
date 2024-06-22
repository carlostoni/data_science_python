class AlunosNotas:
    def __init__(self):
        self.alunos = [
            [[1,2,3],[7,2,3],[1,2,3]],
            [[1,2,3],[7,2,3],[1,2,3]],
            [[1,2,3],[7,2,3],[1,2,3]],
            [[1,2,3],[7,2,3],[1,2,3]],
            [[1,2,3],[7,2,3],[1,2,3]]
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

    if escolha == '1':
        for i in range(3):
            print(mod(dados[i]))
    elif escolha == '2':
        for i in range(3):
            print(media(dados[i]))
    elif escolha == '3':
        for i in range(3):
            print(mediana(dados[i]))
    elif escolha == '4':
        for i in range(3):
            print(desvio(dados[i]))
    elif escolha == '5':
        for i in range(3):
            print(var(dados[i]))
    elif escolha == '6':
        for i in range(3):
            print(amplitude(dados[i]))
    elif escolha == '7':
        for i in range(3):
            print(mod(dados[i]))
            print(media(dados[i]))
            print(mediana(dados[i]))
            print(desvio(dados[i]))
            print(var(dados[i]))
            print(amplitude(dados[i]))
    else:
        print('Opção inválida')

if __name__ == '__main__':
    main()
