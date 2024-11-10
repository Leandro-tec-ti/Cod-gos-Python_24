# Faça um  programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um numero: 1834
# unidade : 4 dezena: 3 centena: 8 milhar: 1

num = int(input("Dígite seu numero:"))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f"Analisando o numero {num}")
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')