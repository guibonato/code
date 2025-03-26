import math
resposta = "sim"
while resposta == "sim":
    a = float(input('Informe o valor de a: '))
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    if a != 0:
        if ((b**2)-(4*a*c)) >= 0:
            x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
            x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
            print(f'As raízes reais são {x1:.3f} e {x2:.3f}')
        else:
            print('O valor de delta deve ser maior que 0')
            continue
    else:
        print('O valor de a deve ser diferente de 0')
        continue


    resposta = input("Deseja continuar? (sim/nao)")

print('Obrigado por usar nosso programa!')