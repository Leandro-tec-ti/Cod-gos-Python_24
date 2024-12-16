# Faça um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos dessa progressão

primeiro = int(input("Primeiro Termo? "))
razao = int(input("Qual é a Razão? "))
decimo = primeiro + (10 - 1) * razao #<<<--- Essa é a formula para achar p décimo termo (Mátematica)
for c in range(primeiro, decimo + razao ,razao):
    print(f"{c}", end=' = ') #<<<--- "end=" é para deixar o código mais bonito.
    