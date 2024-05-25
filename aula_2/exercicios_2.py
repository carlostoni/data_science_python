##1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

# numero = int(input('Digite um numero para ver o su numero ao quadrado '))
# print(numero*numero)

##2 -Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

# nome = input('digite seu nome: ')
# sobrenome = input('digite o seu sobrenome: ')
# print(nome, sobrenome)

##3 -Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

# n1 = []
# n2 = []

# n1.append(int(input('digite um numero ')))
# n2.append(int(input('digite outro numero ')))

# resultado = n1 + n2

# print(resultado)

##4 -Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resulta

# palavra = 'python'
# numero = 1

# print(f'{palavra} {numero}')

##5 -Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

# palavra = 'python e legal'
# palavra_2 = input('digite um palavra ')
# print(palavra, palavra_2)


## ***Exercício 1: Coletando Dados de Experimentos***

# *Você está conduzindo experimentos em um laboratório para analisar o desempenho
# de diferentes modelos de machine learning. Utilize o método append() para adicionar
# os resultados de cada experimento à sua lista de resultados.*

# *resultados_experimentos = []*


# lista_1 = []
# lista_2 = [1,2,5]
# lista_3 = ['nome']
# resultados_experimentos = []

# lista_1.append(input('digite algo'))
# resultados_experimentos.append(lista_1 + lista_2 + lista_3)

# print(resultados_experimentos)

## *Exercício 2: Analisando a Soma de Dados de Vendas*

# *Você está trabalhando com dados de vendas de uma loja online. Utilize o
# método sum() para calcular o total de vendas realizadas durante um período
# de tempo específico.*

# *vendas = [150, 220, 180, 210, 190]*

# vendas = [150, 220, 180, 210, 190]

# print(sum(vendas))

## *Exercício 3 : Identificando o Melhor Modelo de Machine Learning*

# *Você está comparando o desempenho de diferentes modelos de machine
# learning para um problema de classificação. Utilize o método max() para
# encontrar a precisão máxima alcançada pelos modelos.*

# *precisoes = [0.85, 0.92, 0.78, 0.88, 0.90]*

# precisoes = [0.85, 0.92, 0.78, 0.88, 0.90]

# maior = max(precisoes)
# print(maior)

## *Exercício 4: Limpeza de Dados*

# *Você recebeu um conjunto de dados para análise, mas ele está cheio
# de valores nulos e duplicados. Utilize o método clear() para limpar o
# conjunto de dados antes de começar a análise.*

# *dados = [120, 130, None, 140, 120, 150, None]*

# lista= []

# dados = [120, 130, None, 140, 120, 150, None]

# lista = [x for x in dados if x is not None ]
# unico  = list(set(lista))

# print(unico)

# dados.clear()

# print(dados)

## *Exercício 5: Copiando um Conjunto de Dados*

# *Você está trabalhando em um projeto de análise de dados em equipe e precisa
# compartilhar uma versão do conjunto de dados sem modificar o original.
# Utilize o método copy() para criar uma cópia do conjunto de dados.*

# *dados_originais = [35, 40, 45, 50, 55]*

# dados_originais = [35, 40, 45, 50, 55]
# copia = []

# copia = dados_originais.copy()
# print(copia)

## *Exercício 6 : Expandindo o Conjunto de Dados*

# *Durante a análise de dados, você percebe que precisa incluir mais amostras
# para obter resultados mais precisos. Utilize o método extend() para adicionar
# novas amostras ao conjunto de dados existente.*

# *amostras = [0.5, 0.6, 0.7]*

# amostras = [0.5, 0.6, 0.7]
# amostras.extend([0.8])

# print(amostras)

## *Exercício 7: Contando Valores Únicos*

# *Você está explorando um conjunto de dados e deseja contar quantos valores
# únicos existem em uma determinada coluna. Utilize o método count() para contar
# a frequência de cada valor na coluna.*

# *coluna = ["A", "B", "C", "A", "B", "D", "E"]*

# coluna = ["A", "B", "C", "A", "B", "D", "E"]

# for i in range(len(coluna)):
    
#     quantidade = coluna.count(coluna[i])
#     print({coluna[i]}, {quantidade})

## *Exercício 8: Localizando um Registro no Conjunto de Dados*

# *Durante a análise de dados, você precisa encontrar a posição de um
# registro específico no conjunto de dados. Utilize o método index() para localizar
# o registro desejado.*

# *registros = ["ID-001", "ID-002", "ID-003", "ID-004"]*

# registros = ["ID-001", "ID-002", "ID-003", "ID-004"]

# indice = registros.index('ID-001')

# print(indice)

## *Exercício 9 : Inserindo Novos Dados no Conjunto*

# *Durante a análise de dados, você recebe novos registros que
# precisam ser adicionados ao conjunto de dados existente.
# Utilize o método insert() para inserir os novos registros na posição desejada.*

# *registros = ["ID-001", "ID-002", "ID-004", "ID-005"]*

registros = ["ID-001", "ID-002", "ID-004", "ID-005"]

registros.insert(2, 7)
print(registros)  