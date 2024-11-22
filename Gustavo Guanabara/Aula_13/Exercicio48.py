# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de três 
# e que se encontram no intervalo de 1 até 500.

s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(f"Multiplos de 3 = {c}")
        s += c
print(f"A soma foi {s}")