# Exercicio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
#calcule e mostre o comprimento de hipotenusa.
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co **2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hi:.2f}")

#segunda opção para solucionar o problema.
import math # <<<--- com a biblioteca matemática
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca) # <<<--- hipot é para calcular a hipotenusa
print(f"A hipotenusa vai medir: {hi:.2f}")

#Terceira opção para solucionar o problema.
from math import hypot# <<<--- com a biblioteca matemática espefificando o metodo para calcular
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca) # <<<--- hipot é para calcular a hipotenusa
print(f"A hipotenusa vai medir: {hi:.2f}")