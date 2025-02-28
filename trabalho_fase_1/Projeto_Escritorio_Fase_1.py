# Criei listas para facilitar e reduzir as linhas de codigo, dessa forma utilizando os 
# índices para referenciar os meses, consegui torna-lo mais legível e compacto.

lista_temperaturas = [None, None, None, None, None, None, None, None, None, None, None, None]

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
          'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

meses_escaldantes = []


# Desenvolvi duas funções também para que o processo de armazenamento das temperaturas 
# fosse mais eficiente, além de também poder referenciar o inteiro com um mês específico.
def ligar_mes (mes):
    return meses[mes]


def add_temp (mes, temperatura):
    lista_temperaturas[mes-1] = temperatura
    return lista_temperaturas

# Usei de um laço de repetição para que o usuário pudesse informar e alterar as 
# temperaturas quantas vezes desejasse, sem obrigálo a preencher todos os meses

print('Metereologia - Temperatura')
resposta = 's'

while resposta == 's':

    # Utilizei do bloco try/except para garantir que fossem informados dados válidos, 
    # e não haver necessidade de usar de comparadores lógicos, que ocasionaria um código mais extenso.
    try:
        mes = int(input('Informe o mês (1 a 12): '))
        # Garante que seja um mês válido
        if 1 <= mes <= 12:
            temperatura = float(input('Informe a temperatura em Celsius: '))
            if -60 < temperatura < 50:
                add_temp(mes, temperatura)
                resposta = input('Deseja informar mais temperaturas? (s/n) ')
                resposta = resposta.lower()
            else:
                print('Temperatura inválida.')
                resposta = input('Deseja informar alguma temperatura? (s/n) ')
                resposta = resposta.lower()
        else:
            print('Mês inválido.')
            resposta = input('Deseja informar alguma temperatura? (s/n) ')
            resposta = resposta.lower()
    except ValueError:
        print('São admitidos apenas números inteiros para o mês e números reais para a temperatura.')

# Para que o usuario não tivesse a saída forçada do programa, pela caracteristica de o python ser case 
# sensitive, utilizei o método lower para que o programa aceitasse tanto 's' quanto 'S'.

# Aqui criei as variáveis desejadas, para que o programa retornasse cada uma delas, se houvesse alguma ou 
# nehuma temperatura informada.
media = 0
quentes = 0
max = None
min = None
contador_meses = 0

# Neste bloco, usei o laço de repetição da lista (que deverá ter sofrido alterações), de forma que o 
# programa identifique somente os meses que possuem temperatura informada
for mes in lista_temperaturas:
    if mes != None:
        media += mes

        # O metodo index() foi apropriado para que eu criasse a lsita com os meses escaldantes, 
        # e também, para associar os inteiros com os meses.
        if mes > 33:
            meses_escaldantes.append(ligar_mes(lista_temperaturas.index(mes)))
            quentes += 1
        if max == None or mes > max:
            max = mes
            mes_max = ligar_mes(lista_temperaturas.index(mes))
        if min == None or mes < min:
            min = mes
            mes_min = ligar_mes(lista_temperaturas.index(mes))
            # Aqui fiz um contador para poder fazer a média final das temperaturas informadas
        contador_meses += 1
    else:
        continue

    # Essa foi uma linha de código que fiz para evitar o erro de 'Division by zero', caso o usuário nao informasse nada, 
    # mesmo que o propósito do programa seja esse, é um sistema de segurança para evitar crashes.
if contador_meses == 0:
    print('Nenhuma temperatura foi informada.')
    exit() 

media = media / contador_meses

# No final são informados todos os requisitos do projeto, utilziaei o método format para que a saída fosse mais legível e organizada.
print(f'A média das temperaturas é {media:.2f}°C.')
if quentes == 1:
    print(f'{quentes} mês com temperatura superiores a 33°C.')
else:
    print(f'{quentes} meses com temperaturas superiores a 33°C.')
print(f'O mês mais quente foi {mes_max} com {max}°C.')
print(f'O mês mais frio foi {mes_min} com {min}°C.')
