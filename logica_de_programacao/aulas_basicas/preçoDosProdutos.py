resposta = "sim"
while resposta == "sim":
    print('Informe qual o preço de custo do produto')
    valor = float(input())
    if 0 < valor < 10:
        lucro = valor * 1.7
        print(f"Você deve vender o produto a R$ {lucro:.2f}.")
    elif 10 <= valor < 30:
        lucro = valor * 1.5
        print(f"Você deve vender o produto a R$ {lucro:.2f}.")
    elif 30 <= valor < 50:
        lucro = valor * 1.4
        print(f"Você deve vender o produto a R$ {lucro:.2f}.")
    elif valor >= 50:
        lucro = valor * 1.3
        print(f"Você deve vender o produto a R$ {lucro:.2f}.")
    else:
        print("Valor inválido.")
        continue


    resposta = input("Deseja continuar? (sim/nao)")

print('Obrigado por usar nosso programa!')
    