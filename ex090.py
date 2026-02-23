dic = {}
nome = str(input('Nome: '))
media = str(input(f'Média de {nome}: '))
dic = ('Nome': nome, 'Média': media)
if media >= 6:
    dic['Situação'] = 'Aprovado'
else
    dic['Situação'] = 'Reprovado'
print(f'{dic.values()} é igual a {dic["nome"]}')