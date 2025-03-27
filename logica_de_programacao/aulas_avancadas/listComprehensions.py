lista = [1, 2, 3, 4, 5]
quadrados = [item ** 2 for item in lista]
print(quadrados)  
quadrados2 = [item ** 2 for item in lista if item%2==0]
print(quadrados2)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
