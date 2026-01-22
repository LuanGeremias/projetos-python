somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = 0
somamulher = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelo = nome
    if p == 1 and sexo == 'F' and idade < 20:
        somamulher += 1
media = somaidade / 4
print('A média das idades é {}'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('No total, {} mulherer tem menos de 20 anor'.format(somamulher))