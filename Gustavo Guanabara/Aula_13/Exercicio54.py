# Crie um programa que leia o ano de nascimento de sete pessoas no final,
# mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.

from datetime import date #<<<-- importando uma biblioteca para trazer as datas
cont = 0
cont1 = 0
 
for c in range(1, 8):
    atual = date.today().year #<<<-- encontrando a data de hoje (atual)
    nasceu = int(input(f"Qual ano a {c}º pessoa nasceu? "))
    idade = atual - nasceu #<<<-- Formula para encontrar a idade do usuário
    if idade < 21:
        cont += 1
    elif idade >= 21:
        cont1 += 1
print(f"{cont} não é maior de idade. \n{cont1} tem a maioridade. ")