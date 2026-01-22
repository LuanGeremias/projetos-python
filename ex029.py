velo=int(input('Digite a velocidade do \033[34mcarro\033[m: '))
if velo>80:
    velo=velo-80
    print('\033[31mMULTADO\033[m! Você excedeu o limmite de velocidade e foi \033[31mmultado\033[m que custa \033[4:31mR${}\033[m'.format(velo*7))
print('Tenha um bom dia! Digija com segurança!')