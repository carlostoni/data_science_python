import statistics

def desvio(dados):
    resultado = statistics.stdev(dados)
    #print(resultado)
    return resultado