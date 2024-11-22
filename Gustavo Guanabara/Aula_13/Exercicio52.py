# Faça um programa que leia um número inteiro e diga see ele é ou não um número primo.

numero = int(input("Digite um número: "))
total = 0
for c in range(1, numero+1): #<<<--- Importante colocar "+1" no final para dá o número que vc pediu.
    if numero % c == 0: #<<<-- PRIMEIRO PASSO = Fórmula para achar o numero PRIMO
        print("\033[33m", end=' ')# <<<--- "\033[34m" Esses códigos sinalização as cores quando imprimir 
        total += 1
    else:
        print("\033[31m", end=' ')#<<<-- "\033[31m" o mesmo acontece aqui mas com cores diferentes quando imprimir 
    print(f"{c}", end=' ')
print(f"\n\033[m O número {numero} foi divisível por {total} números.")
if total == 2: #<<<-- SEGUNDO PASSO = para saber se é número primo
    print(f"Número {numero} é PRIMO ")
else:
    print(f"Número {numero} não é PRIMO ")