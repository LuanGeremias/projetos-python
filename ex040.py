n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
media=(n1+n2)/2
print('Tirando {:.1f} e {:.1f} fica com a média {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Situação: \033[31mREPROVADO!')
elif media >= 5 and media <=6.9:
    print('Situação: \033[33mRECUPERAÇÃO!')
else:
    print('Situação: \033[34mAPROVADO!')