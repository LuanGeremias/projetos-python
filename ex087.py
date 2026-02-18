numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = 0
for c in range(0, 3):
    for l in range(0, 3):
        numeros[c][l] = int(input(f'Digite um valor para [ {c}, {l} ] '))
        if numeros[c][l] % 2 == 0:
            pares += numeros[c][l]
        if l == 2:
            soma += numeros[c][2]
        if c == 1:
            if l == 0:
                maior = numeros[c][l]
            else:
                if numeros[c][l] > maior:
                    maior = numeros[c][l]
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {numeros[c][l]} ]', end='')
    print()
print('-=' * 30)
print(f'O soma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior número digitado da segunda linha é {maior}')
