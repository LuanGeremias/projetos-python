def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media


num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
print(f'A média das notas é: {media(num1, num2, num3)}')
