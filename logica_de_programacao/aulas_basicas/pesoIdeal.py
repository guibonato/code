print("Vamos saber o seu peso ideal")

sexo = input("Digite o seu sexo (m/f): ")
altura = float(input('Digite a altura em metros: '))

if sexo == "m":
    indice = 72.7 * altura - 58
    print(f'O seu peso ideal sendo homem é {indice}')

if sexo == "f":
    indice = 62.1 * altura - 44.7
    print(f'O seu peso ideal sendo mulher é {indice}')
