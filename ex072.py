numeros = ('zero', 'um', 'dois', 'três',
           'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num2 = int(input('Digite um número entren 0 e 20: '))
while num2 < 0 or num2 > 20:
    num2 = int(input('Número invalido. Digite um número: '))
print(f'Seu número por extensso é {numeros[num2]}')
