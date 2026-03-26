def area(a, b):
    areaa = a * b
    print(f'A area de um terreno {a}x{b} é de {areaa}m²')


print('  Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
