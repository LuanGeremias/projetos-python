fra = str(input('Digite uma frase: ')).strip().upper()
palavras = fra.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('Palindromo!')
else:
    print('Não é um palindromo')