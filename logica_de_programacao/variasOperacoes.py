import math

print('Informe o primeiro valor: ')
a = int(input())

print('Informe o segundo valor: ')
b = int(input())

print('A soma é:', a + b)
print('A diferença é:', (a - b))
print('A média é:', (a+b)//2)
print('A distância é:', math.fabs(a - b))
print('O maior dos dois é:', (a+b+(math.fabs(a-b)))/2)
print('O menor dos dois é:', (a+b-(math.fabs(a-b)))/2)