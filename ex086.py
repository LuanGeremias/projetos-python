numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        numeros[c][l] = int(input(f'Digite um valor para [ {c}, {l} ]: '))
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {numeros[c][l]} ]', end='')
    print()