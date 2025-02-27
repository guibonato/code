import math

print('Metereologia - Temperatura')
resposta = 's'

# Matriz criada para facilitar caso o usuario deseje informar menos de 12 meses
temperaturas = [[] for i in range(12)]

# Laço para incluir quantas temperaturas o usuário desejar em cada mês

while resposta == 's':
    
    mes = int(input('Informe o mês (1 a 12): '))
    # Garante que seja um mês válido
    if 0 < mes <= 12:
        temp = float(input('Informe a temperatura máxima do mês: '))
        # Garante que a temperatura esteja dentro de um valor esperado:
        if -60 <= temp <= 50:
            temperaturas[mes - 1][1] = temp
        else:
            print('Temperatura inválida, digite um valor entre -60 e 50 graus')
    else:
        print('Mês inválido')  
    resposta = input('Deseja informar mais temperaturas? (s/n)')

# Calcula a média
media = 0
