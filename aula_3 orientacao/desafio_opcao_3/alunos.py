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
            return 
