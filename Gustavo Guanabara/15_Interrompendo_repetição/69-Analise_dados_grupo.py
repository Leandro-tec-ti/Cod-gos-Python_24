#  Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
total18 = homens = mulher20 = 0
while True:
    idade = int(input('Sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1 
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '
    while resp not in  'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas maiores de 18 foi {total18}, homens foram {homens} e mulheres Menores que 20 anos foi {mulher20}. ')