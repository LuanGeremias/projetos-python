from random import randint
erros = 1
escolhido = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
while not acertou:
    numero = int(input('Qual é o seu palpite? '))
    if numero == escolhido:
        acertou = True
    else:
        if numero > escolhido:
            print('Menos... Tente novamente:')
        else:
            print('Mais... Tente novamente')
    erros += 1
print('Acertou com {} tentativas. O número era {}. Parabéns!'.format(erros - 1, escolhido))