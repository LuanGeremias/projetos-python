lista = list()
dic = dict()
dic['nome'] = str(input('Nome: ')).strip()
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
if dic['média'] >= 7:
    dic['Situação'] = 'Aprovado'
else:
    dic['Situação'] = 'Reprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')
