from math import pow
n1=float(input('Digite seu peso: '))
n2=float(input('Digite sua altura: '))
imc=n1/pow(n2,2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc <30:
    print('Sobrepeso')
elif imc >=30 and imc<40:
    print('Obesidade')
else:
    print('Obesidade mórbida')