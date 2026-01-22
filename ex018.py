from math import sin,cos,tan, radians
n1=float(input('Digite o angulo: '))
seno=sin(radians(n1))
cos=cos(radians(n1))
tan=tan(radians(n1))
print('O angulo de {} tem o de seno {:.2f}. \nO cosseno de {:.2f}. \nA tangente de {:.2f}'.format(n1, seno, cos, tan))