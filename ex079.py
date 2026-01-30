valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplo! Não vou adicionar...')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp in 'Nn':
        break
print('=-' * 30)
valores.sort()
print(f'Os valores digitados foram {valores}')
