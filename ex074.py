from random import randint
aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for c in aleatorio:
    print(f'{c}', end=' ')
print(f'\nO maior número sorteado foi {max(aleatorio)} e o menor foi {min(aleatorio)}')