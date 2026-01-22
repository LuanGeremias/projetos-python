num2 = 1
num = int(input('Digite um número: '))
while num != 1:
    print(num,' x ', end=' ')
    num2 = num * num2
    num -= 1
print('1 = {}'.format(num2), end='' )