import math

print('Diga quanto tempo durou o evento em segundos')
segundos = int(input())

resto_minuto = segundos%60
minuto = segundos//60
resto_hora = minuto%60
hora = minuto//60

if hora > 0:
    print(f'O evento durou {hora}h, {resto_hora}m e {resto_minuto}s')
elif minuto > 0:
    print(f'O evento durou {minuto}m e {resto_minuto}s')
else:
    print(f'O evento durou {resto_minuto}s')