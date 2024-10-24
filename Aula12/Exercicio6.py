#faça uma variavel sorte onde ela multiplica o ataque por até 20 de ambos os personagens. aumente a vida deles em 10x

import time, random

aventureiro = [
    ["Vida", "Ataque"],
    [1000, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [600, 20]
]

while assaltante[1][0] > 0 and aventureiro [1][0] > 0:
    variante_aventureiro = random.randint(1,20)
    variante_assaltante = random.randint(1,20)
    assaltante[1][0] -= 20 * variante_aventureiro
    aventureiro[1][0] -= 20 * variante_assaltante
    print("status aventureiro")
    for  linha in aventureiro:
        print(linha)
    print(f"multiplicador de critico:", variante_aventureiro)
    print("status assaltante:")
    for linha in assaltante:
        print(linha)
    print(f"multiplicador de critico:", variante_assaltante)
    time.sleep(4)

# corrigir

import time
import random
aventureiro = [
    ["Vida", "Ataque base"],
    [1000, 20]
]
assaltante = [
    ["Vida", "Ataque base"],
    [600, 20]
]

while assaltante[1][0] > 0 and aventureiro[1][0] > 0:
    Variavelaventureiro = random.randint(1, 20)
    Variaveassaltante = random.randint(1, 20)
    assaltante[1][0] -= 20 * Variaveassaltante
    aventureiro[1][0] -= 20 * Variaveassaltante
    print("Status aventureiro:")
    for linha in aventureiro:
        print(linha)
    print(f"multiplicador de critico:", Variavelaventureiro)
    print("Status assaltante:")
    for linha in assaltante:
        print(linha)
    print(f"multiplicador de critico:", Variaveassaltante)
    time.sleep(4)
