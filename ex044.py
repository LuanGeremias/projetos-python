n1=float(input('Digite o preço do produto R$'))
n2=int(input('''Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção? '''))
if n2 == 1:
    des=n1 - (n1 * 10) / 100
elif n2 == 2:
    des=n1 - (n1 * 5) / 100
elif n2 == 3:
    des= n1
    par= n1 / 2
    print('Sua compra sera dividida em duas parcelas de {:.2f}'.format(par))
elif n2 == 4:
    des=n1 + (n1 * 20) / 100
    n3=int(input('Em quantas vezes deseja parcelar? '))
    par = des / n3
    print('Sua compra sera dividida em {} parcelas de R${:.2f}'.format(n3, par))
else:
    print('Você tem que digitar um número entre 1 e 4.')
    des=n1
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(n1, des))
