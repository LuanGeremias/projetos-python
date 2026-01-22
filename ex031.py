km=float(input('Quantos \033[31mkm\033[m vai ser a viagem? '))
if km<=200:
    print('O preço a pagar é \033[31mR${:.2f}\033[m'.format(km*0.50))
else:
    print('O preço a pagar é \033[31mR${:.2f}\033[m'.format(km*0.45))