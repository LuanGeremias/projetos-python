n1=float(input('Digite um número para o lado do triangulo: '))
n2=float(input('Digite outro número para o lado do triangulo: '))
n3=float(input('Digite mais um número para o lado do triangulo: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Esses números formao um \033[34mtriangula\033[m!')
else:
    print('Esses números não formao um \033[31mtriangulo\033[m );')