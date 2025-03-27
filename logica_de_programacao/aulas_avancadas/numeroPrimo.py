def metade_impar (num):
    metade = num%2
    if metade == 0:
        return False
    elif metade == 1:
        return True

def divisores (num):
    lista_div = []
    for i in range(3, num//2 + 1, 2):
        if num%i == 0:
            lista_div.append(i)
    return lista_div

resposta = "s"
while resposta == "s":
    num = int(input("Digite um número para sabermos se é primo: "))
    if num <= 1:
        print("Só serão aceitos números maiores que 1.")
        resposta = input("Você gostaria de tentar outro número? (s/n) ")
    elif num == 2:
        print("O número 2 é o único primo par, além de ser o menor deles.")
        resposta = input("Você gostaria de tentar outro número? (s/n) ")
    else:
        if metade_impar(num) == False:
            print('Este é um número par, logo não é primo.')
            resposta = input("Você gostaria de tentar outro número? (s/n) ")
            
        elif metade_impar(num) == True:
            lista_de_numeros = divisores(num)
            if lista_de_numeros:
                lista_str = ', '.join(map(str, lista_de_numeros))
                print(f'Os numeros que dividem ele são: {lista_str}')
                resposta = input("Você gostaria de tentar outro número? (s/n) ")
            else:
                print("Este número é primo.")
                resposta = input("Você gostaria de tentar outro número? (s/n) ")