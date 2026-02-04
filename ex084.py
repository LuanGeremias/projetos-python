galera = list()
dados = list()
pesados = list()
leves = list()
cont = 0
while True:
    galera.append(str(input('Nome: ')))
    galera.append(float(input('Peso: ')))
    dados.append(galera[:])
    galera.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao total foram {len(dados)} cadrastrados.')
for p in dados:
    if cont == 0:
        pesados.append(p)
        leves.append(p)
    elif p[1][] >
    cont += 1
print(pesados)