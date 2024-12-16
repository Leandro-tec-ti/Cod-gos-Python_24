# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Digite três numeros: ')
a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
# Verificando quem é o menor
menor = a
if b<a and b<c: #<<<---resolvndo a quem é o menor
    menor = b
elif c<a and c<b:
    menor = c
print(f'O menor valor digitado é: {menor}')
#verificando qual é o maior numero
maior = a
if b>a and b>c:# <<<-- resolvendo quem é o maior
    maior = b
elif c>a and c>b:
    maior = c
print(f"O maior valor digitado é: {maior}")
