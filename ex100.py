from random import randint
lista = list()
def sorteia():
    print(f'Sorteando os valores da lista: ', end=' ')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[c]}', end=' ')
    print('PRONTO!')
def somaPar(lis):
    soma = 0
    for c in range(0, len(lis)):
        if lis[c] % 2 == 0:
            soma += lis[c]
    print(f'Somando os valores pares de {lista}, temos {soma}')
sorteia()
somaPar(lista)