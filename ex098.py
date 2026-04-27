from time import sleep
def contagem(inicio, final, contagem):
    if contagem < 0:
        contagem = +contagem
    print(f'Contagem de {inicio} até {final} de {contagem} em {contagem}')
    if inicio < final:
        for c in range(inicio, final + 1, contagem):
            sleep(0.1)
            print(c, end=' ')
    elif inicio > final:
        while inicio >= final:
            sleep(0.3)
            print(inicio, end=' ')
            inicio -= contagem


print('=-' * 20)
contagem(1, 10, 1)
print()
print('=-' * 20)
contagem(20, 0, -2)