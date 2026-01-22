contidade = conthomens = contmulher = 0
while True:
    print('_' * 20)
    print('CADRASTE UMA PESSOA')
    print('_' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    print('_' * 20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {conthomens} homens cadrastrados.')
print(f'E temos {contmulher} mulher com menos de 20 anos.')
