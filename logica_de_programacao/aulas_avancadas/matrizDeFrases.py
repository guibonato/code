matriz = []

for i in range(3):
    frase = input("Digite uma frase: ")
    palavra = frase.split()
    matrizdefrases = []
    for palavras in palavra:
        matrizdefrases.append(palavras)
    matriz.append(matrizdefrases)

print(matriz)