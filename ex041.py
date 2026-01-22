from datetime import date
ano=int(input('Qual é o seu ano de \033[34mnascimento\033[m? '))
date=date.today().year
nas=date-ano
print('O atleta tem {} anos.'.format(nas))
if nas<=9:
    print('Classificação: MIRIM')
elif nas<=14:
    print('Classificação: INFANTIL')
elif nas<=19:
    print('Classificação: jUNIOR')
elif nas<=20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')