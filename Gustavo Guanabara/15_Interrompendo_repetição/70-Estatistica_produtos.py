# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print("-" * 30)
print("Loja do Leandrão")
print("-" * 30)

total = total1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input("Qual é o nome do Produto? "))
    preco = float(input("Qual é o preço do produto? R$: "))
    cont += 1
    total += preco
    if preco >= 1000:
        total1000 += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f"Total da compra foi R${total:.2f} e {total1000} custam mais de R$:1.000, o produto mais barato é {barato}.  ")
