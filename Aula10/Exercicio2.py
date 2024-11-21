# Faça um programa que entre 20 e 50 gere 4 numeros aleatorios e depois os ordena de forma decrescente.

import random

numero1 = random.randint(20, 50)
numero2 = random.randint(20, 50)
numero3 = random.randint(20, 50)
numero4 = random.randint(20, 50)



if numero1 > numero2:
        numero1, numero2 = numero2, numero1
if numero1 > numero3:
        numero1, numero3 = numero3, numero1
if numero1 > numero4:
        numero1, numero4 = numero4, numero1
if numero2 > numero1:
        numero2, numero1 = numero1, numero2
if numero2 > numero3:
        numero2, numero3 = numero3, numero2
if numero2 > numero4:
        numero2, numero4 = numero4, numero2
if numero3 > numero1:
        numero3, numero1 = numero1, numero3
if numero3 > numero2:
        numero3, numero2 = numero2, numero3
if numero3 > numero4:
        numero3, numero4 = numero4, numero3
if numero4 > numero1:
        numero4, numero1 = numero1, numero4
if numero4 > numero2:
        numero4, numero2 = numero2, numero4
if numero4 > numero3:
        numero4, numero3 = numero3, numero4
print(F"Os numeros decrescente são:\n {numero1}\n {numero2}\n {numero3}\n {numero4}")


#segunda Alternativa

#Gerando 4 numeros aleatorios e armazenando em lista
numeros= [random.randint(20, 50)for i in range(4)]

#exibindo os numeros gerados:
print(f"numeros gerados: {numeros}")

#ordenando os numeros com a função sort
numeros.sort()
numeros.reverse()

print(f"Numeros ordenado:{numeros}")
