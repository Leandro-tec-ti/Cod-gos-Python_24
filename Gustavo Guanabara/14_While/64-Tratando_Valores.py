# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0  #---
cont = 0 #   | <<--- eu posso fazer com uma linha atribuição de todas as variaveis EX: (num = cont = soma = 0)
soma = 0 #---
num = int(input('Digite um numero: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero: '))
print(f'Você digitou {cont} numeros e soma entre eles é {soma} ')