# Jogo do palpite:  O sistema gera 1 numero aleatorio entre 1 e 200. o ususario tem 10 papites para tentar acertar.
#o sistema sempre dá um feedback dizendo se o "numero secreto" é maior ou mneor que o palpite do usuario.

import random

numero_aleatorio = random.randint(1, 200)
print(f"{numero_aleatorio}")
for i in range(10):
    palpite = int(input("digite seu numero:"))
    if(palpite > numero_aleatorio+10):
        print(" numero esta muito distante ")
    elif(palpite > numero_aleatorio+5):
        print("seu numero esta muito proximo")
    elif(palpite < numero_aleatorio+5):
        print(" seu numero esta perto ")
    elif(palpite < numero_aleatorio+10):
        print("seu numero esta longe")
    else:
        print("parabens voce acertou")
print("voce não acertou ")

#OBSERVÇÃO: PRECISO AJUSTAR PARA ENTENDER O " < " E " > " NESSA ATIVIDADE
