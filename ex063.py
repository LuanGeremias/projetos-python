print('-==' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('-==' * 10)
num = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print('{} {} '.format(t1,t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' {} '.format(t3), end='')
    cont += 1
print('Fim')