# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Eu sorteei os Valores ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO valor maior sorteado foi: {max(num)}') # <<-- Facilitar para encontrar o maior número com "max()".
print(f'O valor menor sorteado foi: {min(num)}')  # <<-- Facilitar para encontrar o menor número com "mim()".
