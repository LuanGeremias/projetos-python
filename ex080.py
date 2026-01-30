numeros = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        print('Numero adicionado a primeira posição')
        numeros.append(num)
    if c == 1:
        if num > numeros:
