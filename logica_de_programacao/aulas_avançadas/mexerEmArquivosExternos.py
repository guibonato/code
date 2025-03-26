try:
    with open('dados.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")
