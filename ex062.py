primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print(primeiro, end=' > ')
    cont +=1
    primeiro += razao
print('Pausa')
termos = 1
cont2 = 0
while termos != 0:
    cont = 1
    termos = int(input('\nQuantos termos você quer mostrar: '))
    cont2 += termos
    while cont <= termos:
        print(primeiro, end = ' > ')
        primeiro += razao
        cont += 1
print('Prograssão finalizada com {} termos'.formart(cont2 + 10))