# Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: uma espada, uma porção e um escudo. ao longo da aventura encontre um arco no chão e 
#precisa decidir se coloca na mochila ou não. caso coloque, precisará descartar outro intem a sua escolha. 
# Faça um programa simulando essa historia e decisão usando lista/ "if in"

inventario = ["espada","escudo","poçao"]
print("inventario Inicial", inventario)
pergunta = input("voce encontrou um arco em uma clareira. Deseja adicioná-lo ao inventario?\n")
if pergunta == "s":
    print("voce precisa remover um item do inventario para carregar o arco.")
    item = input("Qual item voce deseja remover do inventario?\n").lower()

    #verificando se item existe no inventario
    if item in inventario:
        inventario.remove(item)
        inventario.append("arco")
        print(f"seus novos itens: {inventario}")
        print(f"voce removeu {item} e agora esta carregando um arco.")
    else:
        print(f"o item'{item}' não está no inventario. nada foi removido.")
else:
    print(f'voce decidiu não pegar o arco e continou a sua jornada.')

