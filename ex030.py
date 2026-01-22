n1=int(input('Digite um número: '))
if n1 % 2 == 0:
    print('Este número {} é \033[4:35mimpar\033[m'.format(n1))
else:
    print('Este número {} é \033[4:36mpar\033[m'.format(n1))
print('\033[31mFIM\033[m')