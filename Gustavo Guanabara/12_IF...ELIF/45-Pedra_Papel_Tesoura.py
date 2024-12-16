# Crie um programa que faça o computador jogar JOKENPÔ com você.
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Digite a sua jogada? '))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print(f'Computador jogou {itens[pc]}.')#<<<--- Formula para o computador escolher o que esta escrito na lista
print(f'Você jogou {itens[jogador]}')

if pc == 0:  #computador jogou pedra
    if jogador == 0:
        print("Empate! ")
    elif jogador == 1:
        print("Você ganhgou! ")
    elif jogador == 2:
        print("Você perdeu! ")
    else:
        print("Jogada Invalida! ")
    
elif pc == 1:   # computador jogou papel
    if jogador == 0:
        print("Você perdeu! ")
    elif jogador == 1:
        print("Empate! ")
    elif jogador == 2:
        print("Você ganhgou! ")
    else:
        print("Jogada Invalida! ")
    
elif pc == 2:    # computador jogou tesoura
    if jogador == 0:
        print("Você ganhgou! ")
    elif jogador == 1:
        print("Você perdeu! ")
    elif jogador == 2:
        print("Empate! ")
    else:
        print("Jogada Invalida! ")
      
