#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0 
while True:
    jogador = int(input('Digite seu número: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/N]')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print("Você Ganhou.")
            v += 1 
        else:
            print('Você perdeu.')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Você Ganhou.')
            v += 1 
        else:
            print('Você Perdeu. ')
            break
    print("Vamos jogar novamente? ")
print(f'Voê ganhou {v} Consegutivas.')