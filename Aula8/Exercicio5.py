#faça um programa que diga quais dos 20 primeiros numeros multiplos de 5 são pares
resultado = 0
for i in range(5, 101, 5):
    if i % 2 == 0: #<<<--- Importante sinal de "%" ele é equivalente a
        print(f"multiplos de 5 sao: {i}")
    elif i % 2 != 0:
        resultado += i
print(f"esse é o resultado da soma dos impares: {resultado}")