valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valor)} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
