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
print(" _ ".join(palavra_secreta))
while vidas != 0:
    
    
    
    
    """ letra = str(input("Digite uma letra: "))
    if letra in palavra:
        for i in range(len(palavra)):
            if letra == palavra[i]:
                palavra_secreta[i] = letra
        print(" _ ".join(palavra_secreta))
    else:
        vidas -= 1
        print(f"Você errou! Restam {vidas} vidas.") """