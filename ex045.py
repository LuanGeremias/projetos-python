from time import sleep
from random import choice
print('-=' * 5)
print(' JOKENPÔ ')
print('-=' * 5)
n1=str(input('Você vai jogar pedra, papel ou tesoura? ')).strip().lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lista=['pedra', 'papel', 'tesoura']
sor=choice(lista)
if n1 == sor:
    print('\033[31mEMPATOU\033[m! Eu também escolhi {}'.format(sor))
elif n1 == 'pedra' and sor == 'papel':
    print('\033[31mGANHEI\033[m! Escolhi papel')
elif n1 == 'papel' and sor == 'pedra':
    print('\033[34mPERDI\033[m! Escolhi pedra')
elif n1 == 'papel' and sor == 'tesoura':
    print('\033[31mGANHEI\033m! Escolhi tesoura')
elif n1 == 'pedra' and sor == 'tesoura':
    print('\033[34mPERDI\033[m! Escolhi tesoura')
elif n1 == 'tesoura' and sor == 'pedra':
    print('\033[31mGANHEI\033[m! Escolhi pedra')
elif n1 == 'tesoura' and sor == 'papel':
    print('\033[34mPERDI\033[m! Escolhi papel')
else:
    print('\033[31mPalavra errada, tenta novamente')
