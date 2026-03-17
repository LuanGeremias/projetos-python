jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('-' * 40)
for v, i in enumerate(jogadores):
    print(f'   {v} {i["nome"]}     {i["gols"]}')
print('-' * 30)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"]}')
    for k, v in enumerate(jogadores[resp]["gols"]):
        print(f'   No jogo {v} fez {jogadores[resp]["gols"]} gols')
print('< ENCERRADO >')