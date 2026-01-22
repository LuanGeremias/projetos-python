primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
print('Os primeiros 10 numeros da PA')
while cont != 11:
    print('{} '.format(primeiro), end=' ')
    cont += 1
    primeiro += razao