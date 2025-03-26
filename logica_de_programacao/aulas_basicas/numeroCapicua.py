print('Informe um número inteiro de quatro dígitos: ')

num = str(input())
num_inv = num[::-1]

if num == num_inv: print(f'É um número capicua.({num})')
else: print(f'Não é um número capicua.({num} & {num_inv})')