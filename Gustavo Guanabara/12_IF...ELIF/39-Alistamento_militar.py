# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade, 
# se ele ainda ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo.
# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.
from datetime import date
from time import sleep

atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade =  atual - nascimento
if idade == 18:
    sleep(1)
    print(f"Com {idade} Anos, sim, Você deve se alistar IMEDIATAMENTE! ")
    
elif idade < 18:
    diferenca = 18 - idade
    sleep(1)
    print(f"Você é muito novo e com {idade} Anos, Ainda faltam {diferenca} anos para o alistamento ")
    ano = atual + diferenca
    print(f'O seu alistamento será em {ano}')
else:
    diferenca = idade - 18
    sleep(1)
    print(f"Com {idade} Anos, Já passou da idade e deveria ter se alistado há {diferenca} anos. ")
    ano = atual - diferenca
    print(f'Seu alistamento foi no ano {ano}')