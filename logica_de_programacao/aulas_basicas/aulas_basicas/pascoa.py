print('Data da Páscoa')

ano = int(input('Digite o ano: '))

a = ano % 19
b = ano % 4
c = ano % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dia = 22 + d + e
if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
    dia -= 7
if dia <= 31:
    print(f'A Páscoa do {ano} será no dia {dia} de março.')
else:
    print(f'A Páscoa do {ano} será no dia {dia - 31} de abril.')