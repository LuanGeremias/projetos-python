cont = -2
cont2 = -1
listagem = 'Lápis', 1.70, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
for c in range(0, len(listagem)):
    cont += 2
    cont2 += 2
    print(listagem[cont], end=' ')
    print(listagem[cont2])
