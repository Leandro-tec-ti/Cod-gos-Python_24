# Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: uma espada, uma porção e um escudo. ao longo da aventura encontre um arco no chão e 
#precisa decidir se coloca na mochila ou não. caso coloque, precisará descartar outro intem a sua escolha. 
# Faça um programa simulando essa historia e decisão usando lista/ vetor

nome = input("Qual é o nome do aventureiro? ")

print(f"Aventureiro {nome}, voce esta com a sua mochila e dentro dela tem 3 itens:")
poderes = ["Espada", "escudo", "escudo"]
print("viajando pela estrada acabou de encontrar um novo poder, Arco ")
podernovo = "Arco"
print("Para utilizar esse poder terá que retitar um de dentro da sua mochila,")
desejo = input("qual objeto deseja retirar da mochila? ")
print("primeiro poder", poderes[0])
poderes.append(podernovo)
print(f"sua nova lista de poder {nome} é: {podernovo}", poderes)
poderes.remove(desejo)
print(f'Sua nova lista depois de substituir é : {podernovo}', poderes)


#segunda Alternativa

itens = ["espada", "poção", "escudo"]
print(f"Seus itens são: {itens}")
arco_adicional = input("Digite arco para colocar na mochila\n")
if arco_adicional == "arco":
    print("Arco adicionado!")
    itens.append(arco_adicional)
    remover_item = input("Qual item deseja remover?\n").lower()
    itens.remove(remover_item)
    print(f"A sua lista atual com o arco encontrado",itens)
else:
    print("Continue a sua jornada sem o arco!")