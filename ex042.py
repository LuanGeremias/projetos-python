n1=float(input('Digite um lado de um \033[33mtriângulo\033[m: '))
n2=float(input('Digite mais um lado de um \033[33mtriângulo\033[33m: ' ))
n3=float(input('Digite outro lado de um \033[33mquadrado\033[m: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Esses valores formam um \033[33mtriangulo\033[m!')
if n1 == n2 == n3:
    print('Esses valores formam um \033[33mtriângulo\033[m Equilátero!')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('Esses valores formam um \033[33mtriângulo\033[m Isósceles!')
else:
    print('Esses valores formam um \033[33mtriângulo\033[m Escaleno!')
