print("Informe um numero: ")

num = int(input())

if num < 0: print("O numero informado e negativo")
if num > 0: print("O numero informado e positivo")
if num == 0: print("O numero informado e zero")

num1 = int(input("Agora vamos comparar, informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if num1 > num2 and num1 > num3: maior = num1
if num2 > num1 and num2 > num3: maior = num2
if num3 > num1 and num3 > num2: maior = num3
print("O maior numero informado foi: ", maior)