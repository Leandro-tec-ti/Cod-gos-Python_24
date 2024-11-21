# A Confederação de naciaonal de natação precisa de um progrma que leia o ano de nascimento de um atleta e mostra
# sua categaria, de acordo com idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: SÊNIOR
# Acima: MASTER

from datetime import date

atual = date.today().year
nascimenmto = int(input('Digite o Ano que nasceu: '))
idade = atual - nascimenmto

if idade <= 9:
    print(f'Com {idade} Anos, você é da categoria MIRIM. ')
elif 9 < idade <= 14:
    print(f'Com {idade} Anos, você é da categoria INFANTIL. ')
elif 14 < idade <= 19:
    print(f'Com {idade} Anos, você é da categoria JUNIOR. ')
elif 19 < idade <= 25:
    print(f'Com {idade} Anos, você é da categoria SÊNIOR. ')
else:
    print(f'Com {idade} Anos, você é da categoria MASTER. ')
