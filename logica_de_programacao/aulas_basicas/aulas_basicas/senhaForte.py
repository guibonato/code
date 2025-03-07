import string

print("Verificação de senha forte")

senha = input("Digite a senha: ")
resposta = True

minusculo  = False
maiusculo = False
hash = False
numero = False

if len(senha) < 8:
    resposta = False
    exit(print("Senha com menos de 8 caracteres"))

for i in senha:
    if i.islower():
        minusculo = True
    if i.isupper():
        maiusculo = True
    if i.isnumeric():
        numero = True
    if i in string.punctuation:
        hash = True

if minusculo == False:
    print("A senha não possue caracteres minúsculos")
if maiusculo == False:
    print("A senha não possue caracteres maiúsculos")
if numero == False:
    print("A senha não possue caracteres numéricos")
if hash == False:
    print("A senha não possue caracteres especiais")

if  (minusculo == True and maiusculo == True and 
     numero == True and hash == True):
    print('Esta é uma senha forte.')