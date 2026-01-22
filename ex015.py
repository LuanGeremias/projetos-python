dias=int(input('Quantos dias alugado? '))
km=float(input('Quantos km rodados? '))
s=(dias*60)+(km*0.15)
print('O total a pagar é: R${:.2f}'.format(s))