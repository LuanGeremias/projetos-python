s = 0
print('Qual é a soma dos números entre 1 e 500 que são impares e multiplos de 3?')
for c in range(3, 501, 2):
    if c % 3 == 0:
        s = s + c
print('A soma de todos os números é {}'.format(s))