totmenor = 0
tot = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(c)))
    if c == 1:
        tot = peso
        totmenor = peso
    else:
        if peso > tot:
            tot = peso
        if peso < totmenor:
            totmenor = peso
print('O maior peso lido foi de {}kg'.format(tot))
print('O menor peso lide foi de {}kg'.format(totmenor))
