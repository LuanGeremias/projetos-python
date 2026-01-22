print('=-' * 15)
print('-----EMPRÉSTIMO BANCÁRIO-----')
print('=-' * 15)
valor=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual é o salário do comprador? R$'))
anos=int(input('Quantos anos deseja pagar? '))
mensal=valor / (anos * 12)
negado=(salario*30)/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, mensal))
if mensal >= negado:
    print('Seu empréstimo foi \033[31mnegado\033[m por causa da alta prestação.')
else:
    print('Seu empréstimo foi \033[34maprovado\033[m! E terá que pagar {} por mes!'.format(mensal))