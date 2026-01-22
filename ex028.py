from random import randint
from time import sleep
n1=randint(0,5)
n2=int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(n1, n2))