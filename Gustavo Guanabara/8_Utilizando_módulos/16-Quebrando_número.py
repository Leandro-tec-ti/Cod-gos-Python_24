#Exercicio 16
#faça um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira
# EX: digite um numero: 6.127 o numero 6.127 tem a parte inteiro 6

from math import trunc
num = float(input("Digite um numero: "))
t = trunc(num)
print(f"Seu numero inteiro é: {t}")