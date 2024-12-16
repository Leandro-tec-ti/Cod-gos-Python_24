# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de três 
# e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(f"Multiplos de 3 = {c}")
        cont = cont + 1 #<<<--- conta a quantidade de numeros impares multiplos de 3 (mais um numero que foi achado)
        s += c   #<<<--- faz o calculo dos numeros acomulados 
print(f"A soma foi {s}")
print(f"A quantidade de numeros é: {cont}")