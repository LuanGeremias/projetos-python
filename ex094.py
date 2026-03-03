pessoa = {}
lista = list()
somaidade = cont = 0
while True:
    cont += 1
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Erro! Responda apenas M ou F: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Erro! Responda apenas S ou N ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f' - O grupo tem {len(lista)} pessoas.')
media = somaidade / cont
print(f' - A média de idade é de {media:2} anos.')
print(' - As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print(' - Lista das pessoas que estão acima da média: ')
for c in lista:
    if c['idade'] >= media:
        print(f'   - {c}', end=' ')
        print()

