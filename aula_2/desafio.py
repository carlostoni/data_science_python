# ***Desafio:***

# Voce é um desenvolvedor(a), e precisa criar um sistema de e-commercer: 

# #sistema que tenha formulario
# #estruturas basicas
# #solicitar ao usuário → senha rg cpf email
# #escolher produtos 
# #mensagem despedida após a compra 
# #escolher a forma de pagamento

formulario = []
nome = []
senha = []
rg = []
cpf = []
email = []
compra = []
valor = []

formulario = (f'''{nome.append(input('Digite o seu nome: '))},
{senha.append(input('Digite sua senha: '))}
{rg.append(input('Digite seu rg: '))}
{cpf.append(input('Digite o seu cpf: '))}
{email.append(input('Digite o seu email: '))}''')


produtos_frutas = ['maça', 'banana', 'laranja', 'pera']
produtos_frutas_preco = [2, 3, 1, 2]
produtos_bebidas = ['cha', 'agua', 'coca-cola', 'energetico']
produtos_bebidas_preco = [3, 1, 5, 7]

print('--- iniciar uma compra ---')
opcao = input('sim ou nao: ')

if opcao.lower() == 'sim':
    print('quais itens deseja:')
    for index, pro in enumerate(produtos_frutas):
        print(f'index frutas: {index} = {pro}')
    for index, pro in enumerate(produtos_bebidas):
        print(f'index bebidas: {index} = {pro}')

    opcao = input('vamos comecar pelas frutas, sim ou nao: ')
    if opcao.lower() == 'sim':
        while True:
            
                index_fruta = int(input('digite o índice do produto (ou -1 para parar): '))
                if index_fruta == -1:
                    break
                if 0 <= index_fruta < len(produtos_frutas):
                    compra.append(produtos_frutas[index_fruta])
                    valor.append(produtos_frutas_preco[index_fruta])

                else:
                    print("Índice inválido. Tente novamente.")
    
    opcao = input('deseja adicionar bebidas, sim ou nao: ')
    if opcao.lower() == 'sim':
        while True:
                index_bebida = int(input('digite o índice do produto (ou -1 para parar): '))
                if index_bebida == -1:
                    break
                if 0 <= index_bebida < len(produtos_bebidas):
                    compra.append(produtos_bebidas[index_bebida])
                    valor.append(produtos_bebidas_preco[index_fruta])
                else:
                    print("Índice inválido. Tente novamente.")

print(f'Produtos selecionados: {compra}')
soma = sum(valor)
print(f'o valor total dos produtos e: {soma} ')

print(f'''modos de pagamentos
1- cartao
2- dinheiro
3- pix''')
pagamento = int(input())
if pagamento == 1:
    print("pagamento aprovado")










    
    



    





