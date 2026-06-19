def maior(x, b, y):
    lista = [x, b, y]
    return max(lista)



n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite mais um número: '))
print(f'O maior número digitado foi {maior(n1, n2, n3)}')