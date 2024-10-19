#criando uma lista simples com 3 pokémons
pokemons = ["pikachu", "charmander", "bulbasaur"]

#Exibindo a lista
print("lista de pokémons", pokemons)

#Acessando o primeiro pokemon da lista
print("Primeira pokemon", pokemons[0])

#Adicionando um novo pokemon a lista
pokemons.append("squirtle")
print("Lista de pokemons após adicionar squirtle", pokemons)

#Removendo o pokemons "charmander" da lista
pokemons.remove("charmander")
print("lista de pokemons após remover o charmander", pokemons)

#exibindo o tamanho da lista
print("numero de pokemons na lista", len(pokemons))