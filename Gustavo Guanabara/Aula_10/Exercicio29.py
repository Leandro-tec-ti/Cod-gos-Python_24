# Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km\h, mostre uma mensagem
#dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Qual é a velocidade atual do carro? ')) #<<<-- Desconbrinado a velocidade
if velocidade > 80:
    print('Multado! Você ultrapassou o limite de velocidade permitida que é de 80Km\h')
    multa = (velocidade - 80) * 7   #<<<-- identificando o valor da multa
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança! ')