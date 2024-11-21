# Faça um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0 : Reprovado
# Média entre 5.0 e 6,9: Recuperação
# Média 7.0 ou superior : Aprovado

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

total = (nota1 + nota2) / 2
if total < 5.0:
    print(f'Sua nota de {total} ficou abaixo de 5.0, você está reprovado! ')
elif total > 5.0 and total <= 6.9:
    print(f'Sua nota de {total} ficou acima de 5 e abaixo de 7, você ficou de recuperação! ')
elif total >= 7.0:
    print(f'Parabéns sua nota foi de {total} e você está APROVADO!!! ')
    