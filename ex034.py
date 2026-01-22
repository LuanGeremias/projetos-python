n1=float(input('Digite qual é o seu sálario: '))
if n1>1250:
    print('Seu \033[31msálario\033[m com aumento de 10% fica por {}'.format(n1+((n1*10)/100)))
else:
    print('Seu \033[31msálario\033[m com 15% de aumento fica por {}'.format(n1+((n1*15)/100)))