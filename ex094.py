pessoa = {}
lista = list()
somaidade = cont = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if resp == 'N':
        break
print('-=' * 30)
print(f' - O grupo tem {len(lista)} pessoas.')
media = somaidade / cont
print(f' - A média de idade é de {media} anos.')
print(' - As mulheres cadastradas foram: ', end='')
for c in lista:
    if lista[]['sexo'] in 'F':
        print(pessoa['nome'])
print(' - Lista das pessoas que estão acima da média: ')

