numero = float(input("Digite um número: "))
aprox = float(input("Digite uma raiz aproximada: "))

while abs(aprox ** 2 - numero) > 0.0001:
    aprox = (aprox + numero / aprox) / 2
    print(f'{aprox:.5f}')
