# Melhore o jogo do desafio 028 onde o cumputador vai "pensar" em um numero entre 0 a 10.
# só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint  #<<<--- Bilbioteca com numeros aleatorios
computador = randint(0,10) 
print(f"{computador}")
print("Sou seu computador... acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")
acertou = False #<<<--- criando uma variante
palpites = 0 #<<<-- Criando uma segunda Variante
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("tentei um palpite mais alto.")
        else:
            print("Tente um palipte mais baixo.")
        
    
print(f"parabens voce acertou com {palpites} Tentativas!")