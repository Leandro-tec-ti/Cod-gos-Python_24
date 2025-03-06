# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 
        'jogador2': randint(1,6), 
        'jogador3': randint(1,6), 
        'jogador4': randint(1,6)
        }
ranking = []

print('Valores sorteados')#                ------ <<<--- itemgetter é para colocar em ordem KEYS da lista ou 
for k, v in jogo.items(): #               |              em ordem os valores dentro do Keys, para isso tenho que 
    print(f'{k} tirou o {v} no dado. ')#  |              sinalizar o que estou querendo colocar em ordem EX: itemgetter(1)
    sleep(1)#                             |           
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-'* 30)#                                       |----- <<<--- "reverse=True" serve para inverter a ordem.
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}. ')

