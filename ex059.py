from time import sleep
menu = 0
while menu != 5:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    print('''Escolha no menu qual opção deseja:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    menu = int(input('Qual será a opção? '))
    if menu == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2,soma))
    elif menu == 2:
        mul = num1 * num2
        print('A multiplicação  entre {} e {} é {}'.format(num1, num2, mul))
    elif menu == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
    elif menu == 4:
        menu = 4
    else:
        print('Opção inválida. Tente novamente.')
    print('-==' * 10)
    sleep(1)
print('Fim')
