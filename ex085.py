numeros = list()
pares = list()
impares = list()
for c in range(1, 8):
    n1 = int(input('Digite um valor: '))
    if n1 % 2 == 0:
        pares.append(n1)
    else:
        impares.append(n1)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')
