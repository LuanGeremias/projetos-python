soma = maiscaro = cont = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    soma += preco
    if preco > 1000:
        maiscaro += 1
    if cont == 0 or precobarato > preco:
        maisbarato = nome
        precobarato = preco
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {maiscaro} produtos custando mais de R$1000')
print(f'O produto mais barato foi {maisbarato} que custa R${precobarato:.2f}.')