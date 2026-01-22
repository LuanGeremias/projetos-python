print('=' * 21)
print(' 10 termos de uma PA ')
print('=' * 21)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
for c in range(1, 11):
    print('{} -> '.format(pri), end = ' ')
    pri += raz
print('Acabou')