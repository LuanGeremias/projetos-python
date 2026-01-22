cont = soma = 0
while True:
    numeros = int(input('Digite um número: (999 para parar) '))
    if numeros == 999:
        break
    cont += 1
    soma += numeros
print('Foram {} números digitador ao total e {} sendo a soma.'.format(cont, soma))