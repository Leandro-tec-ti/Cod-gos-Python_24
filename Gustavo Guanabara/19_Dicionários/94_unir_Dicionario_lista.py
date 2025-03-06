# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = {}
total = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ==> '))

    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ==> ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')

    pessoas['idade'] = int(input('Idade: ==> '))
    soma += pessoas['idade']
    total.append(pessoas.copy())
    while True:
        resposta = str(input('Você quer continuar? [S/N] ==> ')).upper()
        if resposta in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == "N":
        break
print(f'A) Ao todo temos {len(total)} pessoas cadastradas. ')
media = soma / len(total)
print(f'B) A Média de idade é de {media:5.2f} anos. ')
print('C) AS mulheres cadastradas foram:', end='')
for p in total:
    if p['sexo'] == 'F':
        print(f',{p["nome"]} ', end='')
print()
print('D) A lista que estão acima da média:', end='')
for p in total:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print(" << ENCERRADO >> ")