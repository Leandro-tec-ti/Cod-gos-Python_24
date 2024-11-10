# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formaum triângulo.

r1 = int(input('Digite o primeira reta '))
r2 = int(input('Digite o segunda reta '))
r3 = int(input('Digite o terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo')
else:
    print('As retas acima não podem formar um triângulo')
