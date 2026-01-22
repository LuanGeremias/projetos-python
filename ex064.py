soma = cont = numeros = 0
cont = int(input('Digite um numero [999 para parar]: '))
while cont != 999:
    soma += cont
    numeros += 1
    cont = int(input('Digite um numero [999 para parar]: '))
print('Foram digitados {} números e a soma de todos é {}'.format(numeros , soma ))