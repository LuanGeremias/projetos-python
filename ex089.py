listona = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listona.append([nome, [nota1, nota2], media])
    resp = ' '
    if resp not in 'NnSn':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'N':
            break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i,a in enumerate(listona):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    mostrarnotas = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if mostrarnotas == 999:
        print('Finalizando...')
        break
    if mostrarnotas <= len(listona) - 1:
        print(f'Notas de {listona[mostrarnotas][0]} são {listona[mostrarnotas][1]}')
    else:
        print('Número invalido!')
print('Volte Sempre!')
