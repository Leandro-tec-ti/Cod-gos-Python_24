# Faça um programa que leia um número qualquer e mostre o seu factorial.
# EX: 5  =  5x4x3x3x = 120

# primeira Alternativa para resolver

#from math import factorial #<<<--- Biblioteca para te dá o numero factorial
#numero = int(input("Digite um numero para calcular o fatorial: "))
#f = factorial(numero)
#print(f"O fatorial de {numero} é {f}")

# segunda Alternativar para resolver
numero = int(input("Digite um numero para calcular o fatorial: "))
contador = numero 
f = 1 #<<< ---  Fatorial sempre ira começar com 1 na variação
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f"{f}")