# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. no fina do programa, mostre:
# A média de idade do grupo.
# Qual é nome do homem mais velho.
# Quantas mulheres tem menos de 20 Anos

soma_idade = 0
media_idade = 0
maioridade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for p in range(1, 3):
    print(f"{p}º pessoa")
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M\F]: ")).strip().upper()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nome_velho = nome

    if  sexo in 'MN' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome   
    if  sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1


media_idade = soma_idade / 4
print(f"Média de idade do grupo é: {media_idade} anos")
print(f"O nome do Homem mais velho: {nome_velho} e a idade: {maioridade_homem} anos")
print(f"Ao todo são {total_mulher_20} mulheres com menos de 20 anos. ")