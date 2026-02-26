lista = list()
dic = dict()
dic['nome'] = str(input('Nome: ')).strip().upper()
dic['média'] = float(input('Média: '))
if dic['média'] >= 7:
    dic['Situação': 'Aprovado']
else:
    dic['Situação': 'Reprovado']
for k, v in dic.items():
    print(f'{k} é igual a {v}')
