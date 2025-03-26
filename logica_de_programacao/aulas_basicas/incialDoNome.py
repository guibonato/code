import string

nome = str(input('Digite o nome completo: '))

inicio = True

for i in nome:
   
    if inicio == True:
        print(f'{i}.', end='')
        inicio = False
    elif i == " ":
        inicio = True