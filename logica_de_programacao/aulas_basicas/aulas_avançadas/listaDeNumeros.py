import random

print('Lista de numeros: ')

lista_num = []

while len(lista_num) < 30:
    numero_aleatorio = random.randint(0, 1500)
    lista_num.append(numero_aleatorio)
    
print(' '.join(map(str, lista_num)))
lista_pares = []
pares = 0

max = 0
for i in lista_num:
    if max < i:
        max = i
    if i % 2 == 0:
        pares += 1
        lista_pares.append(i)
        
print('O maior numero da lista é: ', max)
print(pares, ' numeros pares')
print('Os numeros pares são: ', ' '.join(map(str, lista_pares)))