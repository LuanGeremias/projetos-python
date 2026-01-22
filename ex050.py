s = 0
for c in range(1, 7):
    n1 = int(input('digite o {} número: '.format(c)))
    if n1 % 2 == 0:
        s = s + n1
print('A soma dos valores pares é {}'.format(s))
