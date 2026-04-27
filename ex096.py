def area(largura, comprimento):
    areaa = largura * comprimento
    print(f'A area do terreno é {areaa}²')


lar = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))
area(lar, comp)