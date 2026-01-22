num = int(input('Digite um número: '))
f = 1
for c in range(1, num + 1):
    print(num, end = '')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print(f)