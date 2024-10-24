#O aventureiro encontrou outro assaltante no caminho, mas agora que ele está mais treinado, imediatemente foi para o combate!

#Sabendo que cada personagem tem uma quantidade inicial de "Vida" e um valor de "Ataque". seguindo a seguinte estrutura:

#aventureiro = [
#    ["Vida", "Ataque"],
#    [100, 20]
#]
#assaltante = [
#    ["Vida", "Ataque"],
#    [60, 20]
#]

#A batalha segue as seguintes regras:

#O aventureiro e o assaltante atacam simultaneamente, causando dano um ao outro com o valor de "Ataque".
#A batalha continua até que a "Vida" de um dos personagens chegue a zero ou abaixo.
#Após cada rodada de ataque, o status de cada personagem (seus valores de "Vida" e "Ataque") deve ser exibido.
#Haverá um intervalo de 4 segundos entre as rodadas de ataque para simular a pausa entre os golpes.
#Ao final da batalha, o loop deve parar e os valores finais de "Vida" de ambos os personagens devem ser mostrados.

#Escreva o código para simular essa batalha e exiba o status de ambos os personagens a cada rodada de ataque.

import time, random

aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [60, 20]
]

while assaltante[1][0] > 0 and aventureiro [1][0] > 0:
    variante_aventureiro = random.randint(1,20)
    variante_assaltante = random.randint(1,20)
    assaltante[1][0] -= 20
    aventureiro[1][0] -= 20
    print("status aventureiro")
    for  linha in aventureiro:
        print(linha)
    print("status assaltante:")
    for linha in assaltante:
        print(linha)
    time.sleep(4)

#faça uma variavel sorte onde ela multiplica o ataque por até 20 de ambos os personagens. aumente a vida deles em 10x
    
