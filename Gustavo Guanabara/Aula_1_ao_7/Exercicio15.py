# Exercicio 15
#Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quatidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$:60.00 dia e R$:0.15 por km rodado
dia = int(input("Quantos dias foram utilizado com carro? "))
km = float(input("quantos KM foram percorridos? "))
custo = (dia * 60) + (km * 0.15)
print(f"O valor total da utilização do Veiculo ficou em: {custo:.2f}R$")

