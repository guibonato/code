print('Informe o saldo médio:')

saldo = float(input())

if saldo < 500:
    print('Não há limite')
elif 500 <= saldo < 1000:
    limite = saldo*0.08
    print(f'O limite disponível é de R$ {limite:.2f}')
elif 1000 <= saldo:
    limite = saldo*0.15
    print(f'O limite disponível é de R$ {limite:.2f}')
