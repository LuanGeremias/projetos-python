from time import sleep
def contagem(i, f, t):
    print('-=' * 30)
    if t < 0:
        t = 1
    print(f'Contagem de {i} até {f} de {t} em {t}')
    if i < f:
        for c in range(i, f+1, t):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(i, f-1, -t):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')


contagem(1, 10, 1)
print()
contagem(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
t = int(input('Passo: '))
contagem(i, f, t)