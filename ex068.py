from random import randint
print('=-' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
computador = randint(0, 10)
while True:
    num = int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'IiPp':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('=-' * 15)
    resultado = computador + num
    if resultado % 2 == 0 :
        result = resultado % 2
        ip = 'PAR'
    else:
        result = resultado % 2
        ip = 'IMPAR'
    print(f'Você jogou {num} e o computador jogou {computador}. O total deu {resultado} e deu {ip}')
    if tipo == 'P':
        if resultado % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if resultado % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')