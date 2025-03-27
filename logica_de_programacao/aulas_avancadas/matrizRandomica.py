import random

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 100))
    matriz.append(linha)

print(matriz)

for i in matriz:
    print(i)
    for j in i:
        print(j)