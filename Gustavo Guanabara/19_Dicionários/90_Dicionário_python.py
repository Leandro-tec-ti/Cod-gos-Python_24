# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Qual é seu nome? '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
    print(f'Parabéns {aluno["nome"]}, com a média {aluno["media"]} você está {aluno["situação"]}')

elif 5 <= aluno['media'] < 7:
    aluno['situação'] = "Recuperação"
    print(f'Atenção {aluno["nome"]}, com a média {aluno["media"]} você está {aluno["situação"]}')

else:
    print(f'infelizmente {aluno["nome"]}, com a média {aluno["media"]} você está {aluno["situação"]}')

