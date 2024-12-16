# Descobrir se a Média de um aluno no ano com 4 notas diferentes foi boa ou ruim.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota '))
n3 = float(input('Digite sua terceira nota '))
n4 = float(input('Digite sua quarta nota: '))
media = (n1 + n2 + n3 + n4) /4
if media >= 7.0:
    print(f'Sua média foi: {media} PARABÉNS! Sua nota foi aprovada')
else:
    print(f'Sua média foi: {media} essa nota ficou abaixo da média e não foi aprovada')


#if = se existir (remete a algo verdadeiro)

#else = Caso contrário (remete ao oposto do if) ou (caso não tenha nenhuma outra  condição)


#Desafios
# Exxercicios do 28 ao 35