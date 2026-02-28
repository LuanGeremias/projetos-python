from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
pessoa['idade'] = datetime.now().year - nasc
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')

