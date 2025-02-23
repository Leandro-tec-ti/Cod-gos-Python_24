# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
lista = []
joga = []
print('=-' * 30)
print('                   JOGA NA MEGA SENA             ')
print('=-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0 
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    joga.append(lista[:])
    lista.clear()
    total += 1
print(f'sorteando: {quantidade}')
for i, l in enumerate(joga):
    print(f'Jogo {i+1}: {l}')

