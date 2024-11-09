# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# EX: Ana maria de souza 
# primeiro = Ana
# último = Souza

n = str(input('Digite seu nome completo: ')).strip().upper()
nome = n.split()
print(f"Seu primeiro nome é: {nome[0]}")
print(f'Seu último nome é: {nome[len(nome)-1]}')
