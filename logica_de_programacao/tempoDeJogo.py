print('Duração do jogo.')

hora_inicial = int(input('Informe que hora iniciou o jogo: '))
minuto_inicial = int(input('Informe os minutos: '))
hora_final = int(input('Informe que hora encerrou o jogo: '))
minuto_final = int(input('Informe os minutos: '))

minuto = minuto_final - minuto_inicial
hora = hora_final - hora_inicial

if hora < 0 and minuto > 0:
    hora += 24
    if minuto == 0: 
        print(f'A duração da partida foi de {hora}h')
    else:
        print(f'A duração da partida foi de {hora}h e {minuto}m')

elif hora < 0 and minuto < 0:
    hora += 23
    minuto += 60
    if minuto == 0: 
        print(f'A duração da partida foi de {hora}h')
    else:
        print(f'A duração da partida foi de {hora}h e {minuto}m')

elif minuto < 0:
    hora -= 1
    minuto += 60
    if hora == 0:
        print(f'A duração foi de {minuto}m')
    else:
        print(f'A duração foi de {hora}h e {minuto}m')

elif minuto > 0:
    print(f'A duração da partida foi de {hora}h e {minuto}m')

