resp = 'S'
media = soma = maior = menor = quant = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('A média entre os {} números digitados é {} sendo o maior {} e o menor {}.'.format(quant, media, maior, menor))
