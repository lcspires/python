qtd_pokemons = int(input())

for _ in range(qtd_pokemons):
    dano_base, acrescimo = map(int, input().split())
    print(dano_base + acrescimo)


"""

qtd_pokemons = int(input())

resultados = []

for _ in range(qtd_pokemons):
    dano_base, acrescimo = map(int, input().split())
    resultados.append(dano_base + acrescimo)

# no lugar de um looping de prints:
print("\n".join(map(str, resultados)))

"""
