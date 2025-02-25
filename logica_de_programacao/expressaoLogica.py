print('Expressoes logicas')

num1 = int(input("D5igite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > 0:
    print('Primeira expressao', True)
else:
    print('Primeira expressao', False)

if num3 >= 0 and num3 % 2 == 0:
    print('Segunda expressao', True)
else:
    print('Segunda expressao', False)
    

