import math

print("Calculadora do volume da esfera!")

raio = float(input("Digite o valor do raio da esfera: "))

volume = (4/3)*math.pi*raio**3
""" pode ser tambem (4/3)*math.pi*math.pow(raio, 3) """

print ("O volume é",volume)
