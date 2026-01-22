from datetime import date
nascimento=int(input('Digite a sua data de nascimento: '))
data=date.today().year
ano=data-nascimento
temp=ano-18
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, ano, data))
if ano <= 17:
    temp = 18 - ano
    print('Ainda faltam \033[31m{}\033[m anos para o alistamento'.format(temp))
    print('Seu alistamento será em {}'.format(data+temp))
elif ano == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE')
else:
    print('Você ja deveria ter se alistado há \033[31m{} anos!'.format(temp))
    print('Seu alistamento foi em {}'.format(nascimento+18))

