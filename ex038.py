n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro valor é o \033[31mMAIOR\033[m')
elif n1 < n2:
    print('O segunda valor é o \033[31mMAIOR\033[m')
else:
    print('Todos os números são iguais')

