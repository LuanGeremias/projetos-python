print('=' * 30)
print('BANCO LG')
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$'))
while True:
    if saque >= 50:
        resto = saque % 50
        result =  saque - resto
        print(f'Total de {result // 50} cédulas de R$50')
    resto = saque % 50
    if resto >= 20:
        resto20 = resto % 20
        result = resto - resto20
        print(f'Total de {result // 20} cédulas de R$20')
    resto20 = resto % 20
    if resto20 >= 10:
        resto10 = resto20 % 10
        result = resto20 - resto10
        print(f'Total de {result // 10} cédulas de R$10')
    resto10 = resto % 10
    if resto10 >= 1 or resto20 >= 1 or resto >= 1:
        print(f'Total de {resto10} cédulas de R$1')
    break
print('Volte sempre ao BANCO LG! Tenha um bom dia!')