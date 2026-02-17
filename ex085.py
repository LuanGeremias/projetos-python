numeros = [[], []]
for c in range(1, 8):
    n1 = int(input('Digite um valor: '))
    if n1 % 2 == 0:
        numeros[0].append(n1)
    else:
        numeros[1].append(n1)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')
