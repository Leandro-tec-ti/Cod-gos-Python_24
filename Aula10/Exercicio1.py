# Faça um programa que gere 3 numeros aleaorios (float) entre 1 e 15 e vc tem 1 tentativa de para descobrir qual é o maior.
# Façã um programa que entre 20 e 50 gere 4 numeros aleatorios e depois os ordena de forma decrescente.


import random

numero1 = random.uniform(1, 15)
numero2 = random.uniform(1, 15)
numero3 = random.uniform(1, 15)

print(F"{numero1}{numero2}{numero3}")

for i in range (1):
   
    palpite = int(input(f"Digite Qual tentativa é a mais alta:\n opção: 1\n opção: 2\n opção: 3 \n"))
    if palpite == 1 and (numero1 > numero2) and (numero1 > numero3):
        print("Parabens, você acertou")
    elif palpite == 2 and (numero2 > numero1) and (numero2 > numero3):
        print("Parabens, voce acertou!")
    elif palpite == 3 and (numero3 > numero1) and (numero3 > numero2):
        print("Parabens, voce acertou!")
    else:
        print("Voce errou!")
    print(f"os numeros aleatorios: \n{numero1}, \n{numero2}, \n{numero3}")
        
