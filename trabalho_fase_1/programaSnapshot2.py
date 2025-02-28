lista_temperaturas = [None, None, None, None, None, None, None, None, None, None, None, None]

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
          'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

meses_escaldantes = []

def ligar_mes (mes):
    return meses[mes]


def add_temp (mes, temperatura):
    lista_temperaturas[mes-1] = temperatura
    return lista_temperaturas

print('Metereologia - Temperatura')
resposta = 's'

while resposta == 's':
    
    mes = int(input('Informe o mês (1 a 12): '))
    # Garante que seja um mês válido
    if 1 <= mes <= 12:
        temperatura = float(input('Informe a temperatura em Celsius: '))
        if -60 < temperatura < 50:
            resposta = input('Deseja informar mais temperaturas? (s/n) ')
            add_temp(mes, temperatura)
        else:
            print('Temperatura inválida.')
            resposta = input('Deseja informar alguma temperatura? (s/n) ')

    else:
        print('Mês inválido.')
        resposta = input('Deseja informar alguma temperatura? (s/n) ')

media = 0
quentes = 0
max = None
min = None
contador_meses = 0

for mes in lista_temperaturas:
    if mes != None:
        media += mes
        if mes > 33:
            meses_escaldantes.append(ligar_mes(lista_temperaturas.index(mes)))
            quentes += 1
        if max == None or mes > max:
            max = mes
            mes_max = ligar_mes(lista_temperaturas.index(mes))
        if min == None or mes < min:
            min = mes
            mes_min = ligar_mes(lista_temperaturas.index(mes))
        contador_meses += 1
    else:
        continue
if contador_meses == 0:
    print('Nenhuma temperatura foi informada.')
    exit()

media = media / contador_meses

print(f'A média das temperaturas é {media:.2f}°C.')
if quentes == 1:
    print(f'{quentes} mês com temperatura superiores a 33°C.')
else:
    print(f'{quentes} meses com temperaturas superiores a 33°C.')
print(f'O mês mais quente foi {mes_max} com {max}°C.')
print(f'O mês mais frio foi {mes_min} com {min}°C.')
