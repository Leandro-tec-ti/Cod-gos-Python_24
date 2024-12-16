# Desenvolva um programa que leia seis numeros inteiro e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, o desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f"Digite o {c}° numero: "))
    if numero % 2 == 0: #<<<--- calculo para achar só os números pares
        soma += numero
        cont += 1

print(f"você informou {cont} números pares e a soma foi {soma} .")

