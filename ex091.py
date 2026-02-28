from time import sleep
from random import randint
from operator import itemgetter
rank = dict()
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    sleep(1)
    print(f'  - O {k} tirou {v}')
print('Ranking dos jogadores:')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    sleep(1)
    print(f'  - {i + 1}° lugar: {v[0]} com {v[1]}')
