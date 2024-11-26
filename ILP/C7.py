# Leitura da configuração de entrada
q, forma, ordem = input().split()
q = int(q)

# Lista para armazenar os pokémons
pokemons = []

# Leitura dos pokémons
for _ in range(q):
    entrada = input().split()
    nome = entrada[0]
    nivel = int(entrada[1])
    pokemons.append((nome, nivel))

# Ordenação
if forma == 'N':  # Ordenar por nome
    chave = lambda pokemon: pokemon[0]
elif forma == 'L':  # Ordenar por nível
    chave = lambda pokemon: pokemon[1]

# Determinar a ordem de classificação
if ordem == 'C':  # Crescente
    pokemons.sort(key=chave)
elif ordem == 'D':  # Decrescente
    pokemons.sort(key=chave, reverse=True)

# Saída
for nome, nivel in pokemons:
    print(nome, nivel)
