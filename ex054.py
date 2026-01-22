from datetime import date
data = date.today().year
soma = 0
tot = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if data - ano >= 18:
        soma += 1
    else:
        tot += 1
print('Ao todo tivemor {} pessoas maiores de idade'.format(soma))
print('E também tivemos {} pessoas menores de idade'.format(tot))