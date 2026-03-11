pessoa = {}
lista = list()
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N ')
    if resp == 'N':
        break

print('-=' * 30)
print(f' - O grupo tem {len(lista)} pessoas.')
media = somaidade / len(lista)
print(f' - A média de idade é de {media:5.2f} anos.')
print(' - As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print(' - Lista das pessoas que estão acima da média: ')
for c in lista:
    if c['idade'] >= media:
        print('     ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

