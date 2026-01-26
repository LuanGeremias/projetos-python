cont = cont3 = 0
contpar = 5
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
for c in range(0, 4):
    if num[c] == 9:
        cont += 1
    if num[c] == 3:
        cont3 += 1
print(f'O 9 apareceu {cont} vezes')
if cont3 > 0:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu em nenhuma posição!')
print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')