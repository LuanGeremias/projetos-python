from time import sleep
def maior(* num):
    
    print('-=' * 30)
    maior = num[0]
    print('Analisando os valores passados...')
    sleep(1)
    for c in range(0, len(num)):
        if num[c] > maior:
            maior = num[c]
        print(f'{num[c]}',end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6, 1)
maior(6)
maior()

