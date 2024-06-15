#  3.  Crie uma função chamada `concatenar_nomes` que recebe dois nomes como 
#    argumentos e retorna a concatenação dos dois nomes separados por um espaço. 
#    Em seguida, use essa função para concatenar os nomes "Maria" e "Silva".

def concatenar_nomes(nome1, nome2):

    print(f'{nome1} {nome2}')

    
def main():
    
    nome1 = 'Maria'
    nome2 = 'Silva'
    concatenar_nomes(nome1, nome2)
main()