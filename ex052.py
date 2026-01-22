soma = 0
n1 = int(input('Digite um número: '))
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[31m',end='')
        soma = soma + 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi dividível {} vezes'.format(n1, soma))
if soma == 2:
    print('E por isso ele é um número primo')
else:
    print('E por isso ele NÃo é um número primo')