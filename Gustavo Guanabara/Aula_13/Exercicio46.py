# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifíficio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep
print("Atenção contagem Regressiva! ")
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print("FOGOOOOOO!!!!")