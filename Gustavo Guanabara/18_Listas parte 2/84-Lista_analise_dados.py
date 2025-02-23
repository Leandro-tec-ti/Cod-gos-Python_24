# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
galera = []
maior = menor = 0
while True:
    pessoas.append(str(input('Digite um nome: ')))
    pessoas.append(float(input('Digite seu peso: ')))
    if len(galera) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in "N":
        break
    if resposta not in "S":
        print('Tente novamente ')
print(f'O total de {len(galera)} pessoas cadastradas')#<<--"len()" serve aqui para contabilizar os cadastros
print(f'O maior peso foi de {maior} Kg, Essa é a lista das pessoas mais pesadas: ', end= '')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} ', end='')

print()
print(f'O menor foi de {menor} kg, Essa é a lista das pessoas mais leves: ', end= '')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end='')