#exercicio 10
#Faça um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre a ela quantos dolares e Euro ela pode comprar.
#Considere US$:1.00 = R$:3.27 EU$: 5.51
real = float(input("Quantos Reais você tem na carteira? "))
dolar = real / 3.27
Euro = real / 5.51
print(f"Com {real} Reais, você consegue comprar {dolar:.2f} Dolares e {Euro:.2f} Euros ")
