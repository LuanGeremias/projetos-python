sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidor. Porr favor, enforme seu sexo: [M/F] ')).upper().strip()
print('Sexo {} registrado com susesso!'.format(sexo))
