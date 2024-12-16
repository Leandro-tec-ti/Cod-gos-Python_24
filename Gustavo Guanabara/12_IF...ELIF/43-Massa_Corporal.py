# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, e calcule seu IMC e mostre seu status,
# de acorrdo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# Acima de 40: obesidade mórbida

peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2) #<<<--- base de calculo do IMC ( "** 2" quer dizer ao quadrado)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você ficou Abaixo do peso. ')
elif imc < 25:
    print(f'seu IMC é {imc:.2f} e você esta com peso ideal. ')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso. ')
elif imc < 40: 
    print(f'Seu IMC é {imc:.2f} e você está com obesidade. ')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida. ')
