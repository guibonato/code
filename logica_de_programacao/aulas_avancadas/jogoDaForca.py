import requests

def gerar_palavra_aleatoria():
    response = requests.get("https://api.dicionario-aberto.net/random")
    if response.status_code == 200:
        palavra = response.json()['word']
        return palavra
    else:
        return None

vidas = 5
print("Bem-vindo ao jogo da forca!")
palavra = gerar_palavra_aleatoria()
palavra_secreta = ["_" for letra in palavra]
print(" ".join(palavra_secreta))
banco_de_letras = []
while vidas != 0:
    letra = str(input('Digite uma letra: '))
    if letra in palavra:
        for i in range(len(palavra)):
            if letra == palavra[i]:
                palavra_secreta[i] = letra
        print(' '.join(palavra_secreta))
        if not '_' in palavra_secreta:
            exit('Você ganhou, parabéns!!!!')      
        banco_de_letras.append(letra)
        print('As letras que ja foram são: ' + ', '. join(banco_de_letras))
    else:
        print('Essa letra não tem.')
        banco_de_letras.append(letra)
        print('As letras que ja foram são: ' + ', '. join(banco_de_letras))
        vidas -= 1
        print(f'Você tem {vidas} apenas.')

if vidas == 0:
    print('Que pena você perdeu.')
    
