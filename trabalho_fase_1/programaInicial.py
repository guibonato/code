import math

def criar_mes (mes, temperatura):
    return {mes: temperatura}

print('Metereologia - Temperatura')
resposta = 's'



# Laço para incluir quantas temperaturas aos meses 

while resposta == 's':
    
    mes = int(input('Informe o mês (1 a 12): '))
    # Garante que seja um mês válido
    if mes == 1:
        janeiro = float(input('Informe a temperatura: '))
        if -60 < janeiro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida.')
            continue
    elif mes == 2:
        fevereiro = float(input('Informe a temperatura: '))
        if -60 < fevereiro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 3:
        marco = float(input('Informe a temperatura: '))
        if -60 < marco < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 4:
        abril = float(input('Informe a temperatura: '))
        if -60 < abril < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 5:
        maio = float(input('Informe a temperatura: '))
        if -60 < maio < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 6:  
        junho = float(input('Informe a temperatura: '))
        if -60 < junho < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 7:
        julho = float(input('Informe a temperatura: '))
        if -60 < julho < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 8:
        agosto = float(input('Informe a temperatura: '))
        if -60 < agosto < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 9:
        setembro = float(input('Informe a temperatura: '))
        if -60 < setembro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 10:
        outubro = float(input('Informe a temperatura: '))
        if -60 < outubro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 11:
        novembro = float(input('Informe a temperatura: '))
        if -60 < novembro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    elif mes == 12:
        dezembro = float(input('Informe a temperatura: '))
        if -60 < dezembro < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
        else:
            print('Temperatura inválida')
            continue
    else:
        print('Mês inválido.')
        resposta = input('Deseja informar alguma temperatura? (s/n) ')


                  