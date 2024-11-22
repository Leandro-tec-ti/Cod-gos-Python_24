# Crie um programa que leia o ano de nascimento de sete pessoas no final,
# mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.
s = 0
for c in range(0,7):
    pessoa = int(input("Quantos anos você tem? "))
    if pessoa < 18:
        print(f"Você tem {pessoa} Anos, não é maior de idade")
    elif pessoa > 18:
        print(f"Você tem {pessoa} Anos, você Tem a maioridade")
