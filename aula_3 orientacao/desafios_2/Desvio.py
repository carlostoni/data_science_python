import statistics

def desvio(dados):
    resultado = statistics.stdev(dados)
    print('O desvio padrao é ', resultado)
    return desvio