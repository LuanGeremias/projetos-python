from datetime import date
ano=int(input('Qual ano você quer \033[34manalisar\033[m? Digite 0 para analisar o \033[34mano atual\033[m: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[31mbissexto\033[m'.format(ano))
else:
    print('O ano {} \033[31mnão é bissexto\033[m'.format(ano))