# Jogo do palpite:  O sistema gera 1 numero aleatorio entre 1 e 200. o ususario tem 10 papites para tentar acertar.
#o sistema sempre dá um feedback dizendo se o "numero secreto" é maior ou mneor que o palpite do usuario.

import random

numero_aleatorio = random.randint(1, 100)
print(f"{numero_aleatorio}")
for i in range(10):
    palpite = int(input("digite seu numero:"))
    if((palpite > numero_aleatorio ) and (palpite < (numero_aleatorio +5))):
        print("muito perto, tente um valor menor")
    elif((palpite >= (numero_aleatorio + 5)) and (palpite <= (numero_aleatorio + 10))):
        print(" você está proximo, tente um valor menor ")
    elif(palpite > (numero_aleatorio +10)):
        print("voce digitou muuito acima")
    elif((palpite < numero_aleatorio) and (palpite > (numero_aleatorio - 5))):
        print("muito perto, tente um numero maior")
    elif((palpite <= (numero_aleatorio - 5)) and (palpite >= (numero_aleatorio - 10))):
        print(" voce esta proximo, tente um  numero maior ")
    elif(palpite < (numero_aleatorio - 10)):
        print("seu numero esta Abaixo")
    else:
        print("parabens voce acertou")