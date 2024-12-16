# Faça um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tente
# desconbrir qual foi o numero escolhido pelo computador. o programa devará escrever na tela se usuário venceu ou perdeu.

from random import randint
pc = randint(0,5) # <<<--- Este comando faz o Computador "pensar"

jogador = int(input('Qual será que foi o numero que o computador pensou de 0 a 5? \n')) # jogador tentando advinhar
if jogador == pc:
    print('Parabéns, você Ganhou!!!')

else:
    print(f'Pensei no numero: {pc}\n')
    print('Não foi dessa vez, você Perdeu!!!')