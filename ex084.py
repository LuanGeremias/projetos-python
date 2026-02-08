pessoas = list()
dados = list()
pessoasmaior = list()
pessoasmenor = list()
maior = menor = cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
for p in pessoas:
    cont += 1
    if cont == 1:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]
for p in pessoas:
    if p[1] == maior:
        pessoasmaior.append(p[0])
    elif p[1] == menor:
        pessoasmenor.append(p[0])
print(f'O maior peso foi de {maior}kg. peso de {pessoasmaior}')
print(f'O menor peso foi de {menor}kg. peso de {pessoasmenor}')