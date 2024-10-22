#Enquanto você segue seu caminho na floresta, um bandido armado surge e exige sua poçao.
#Você tem a opção de sacar sua espada e enfrentar o bandidoou entregar a sua poção ao bandido.
#se tentar lutar contra ele sem espada, voce perde a batalha e o jogo. se tiver com ela, ganha e segue o jogo.
#se entregar a poção, voce fica sem e segue o jogo.
#mas se disser que irá entragar a pocao sem tê-la no inventario, o bandido ficará furioso e será fim do jogo.
#caso escolha uma opçao de invalida o bandido se aproveita de sua hesitação e lhe ataca, resultando em fim de jogo.


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

print("Surpresa! Enquanto você segue seu caminho na floresta, um bandido armado surge e exige sua poçao.")
escollha = int(input("O que deseja fazer?\n 1 = sacar sua arma e lutar\n 2 = entregar a poção\n 3 = não fizer nada\n"))

if escollha == 1:
    if "espada" in inventario:
        print("Parabens voce derrotou o bandido, continue a sua jornada")
    else:
        print("infelizmente voce foi derrotado")

elif escollha == 2:
    if "poçao" in inventario:
        inventario.remove("poçao")
        print("voce esta sem a poçao, segue o jogo")
    else:
        print("voce não tem a poçao e o bandido te atacou, fim do jogo")

elif escollha == 3:
    print("voce não tomou uma posição e infelizmente voce foi atacado e perdeu o jogo")

else:
    print("voce nao tomou iniciativa e o bandido te atacou! perdeu o jogo")