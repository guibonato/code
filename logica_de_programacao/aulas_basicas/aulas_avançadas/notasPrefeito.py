import random


print('MVP da NBB 2025')

primeiros_nomes = ["Lucas", "João", "Carlos", "Pedro", "Rafael", 
    "Gabriel", "Matheus", "Felipe", "Thiago", "Bruno", 
    "Gustavo", "Diego", "Fernando", "André", "Rodrigo", 
    "Eduardo", "Henrique", "Leonardo", "Caio", "Victor"]

sobrenomes = ["Silva", "Pereira", "Santos", "Oliveira", "Costa", 
    "Souza", "Ferreira", "Almeida", "Nascimento", "Lima", 
    "Gomes", "Martins", "Rocha", "Ribeiro", "Carvalho", 
    "Barbosa", "Teixeira", "Melo", "Monteiro", "Vieira"]

jogadores = []
print('Jogadores candidatos a MVP (media de participações por jogo):')

for i in range (1, 201):
    nome_completo = random.choice(primeiros_nomes) + " " + random.choice(sobrenomes)
    pontos = random.randint(5, 50)
    assist = random.randint(0, 20)
    rebotes = random.randint(0, 20)
    jogadores.append([nome_completo, pontos, assist, rebotes])
    print(f'{i} - {nome_completo} - Pontos: {pontos} - Assistências: {assist} - Rebotes: {rebotes}')

mvp = [None]
stats = 0

for i in jogadores:
    media = (i[1] + i[2] + i[3]) / 3
    if media > stats:
        mvp = i
        stats = media
        
print(f'O MVP da NBB 2025 é {mvp[0]} com média de {stats:.2f} participações em pontos por jogo.')