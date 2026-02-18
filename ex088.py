from time import sleep
from random import randint
numeros = list()
print('-' * 30)
print('     JOGO DA MEGA SENA')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
if jogos > 0:
    print('-=' * 3, f'SORTEANDO {jogos} jogos', '-=' * 3)
    for i in range(0, jogos):
        sleep(1)
        numeros.clear()
        for c in range(0, 6):
            numeros.append(randint(1, 60))
        numeros.sort()
        print(f'Jogo {i + 1}: {numeros}')
    print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
else:
    print('Número invalido!')
