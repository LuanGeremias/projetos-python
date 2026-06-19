import math
def imc(alt, peso):
    imcc = peso / math.pow(alt, 2)
    return imcc


alt1 = float(input('digite a altura: '))
peso1 = float(input('digite a peso: '))
print(imc(alt1, peso1))