# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada 
# aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in "Nn":
        break
print('=-' *30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' *30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_' * 35)
    opc = int(input('Mostrar nota de qual Aluno? (999 -> Encerra): '))
    if opc == 999:
        print("Finalizando... ")
        break
    if opc <= len(ficha) - 1:
        print(f'notas de ficha de {ficha[opc][0]} são {ficha[opc][1]}')
print('>>>>     VOLTE SEMPRE    <<<<<')