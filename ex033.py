n1=int(input('Digite um número: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite mais um numero: '))
if n1 > n2 > n3:
    maior=n1
    menor=n3
if n1 < n2 < n3:
    maior=n3
    menor=n1
if n2 < n3 < n1:
    maior=n1
    menor=n2
if n1 < n3 < n2:
    maior=n2
    menor=n1
if n2 < n1 < n3:
    maior=n3
    menor=n2
if n3 < n1 < n2:
    maior=n2
    menor=n3
print('O \033[34mmaior\033[m número é {} e o \033[31mmenor\033[m é {}'.format(maior,menor))