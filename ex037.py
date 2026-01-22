num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para convenção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
num2=int(input('Sua opção: '))
if num2 == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(num, bin(num)[2:]))
elif num2 == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif num2 == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opação invalida')
