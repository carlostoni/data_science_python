# Exercício: Calculadora de Área

#    Crie uma função chamada `area_retangulo` que recebe a base e a altura de 
#    um retângulo e retorna a área. Em seguida, use essa função para calcular a área 
#    de um retângulo com base 4 e altura 6.

# def area_retangulo():
#     comprimento = 4
#     altura = 6
#     area = comprimento * altura
#     print(area)
# area_retangulo()

def area_retangulo(al , co):
    area = al * co
    return area

def calculo():
    al = int (input('digite altura '))
    co= int(input('digite comprimento '))
    
    area_retangulo(al, co)
    resultado = area_retangulo(al, co)
    print(resultado)

calculo()