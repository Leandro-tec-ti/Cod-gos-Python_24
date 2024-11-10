# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero: '))
resultado = num % 2 #<<<-- esse é o calculo para descobir o resto da divisão, 
if resultado == 0: #<<<--- se o resto der 0 quer dizer que o numero digitado é PAR
    print(f'O número {num} é PAR ')
else:
    print(f'O número {num} é IMPAR')