# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, 
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Quantos km tem e a sua viagem? '))

if distancia <= 200:
    preco = distancia * 0.50 #<<<--- base do calculo para saber o valor da passagem
    print(f'a Distancia da sua viagem é de {distancia}km e o valor da sua passagem ficou em R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'A distacia da sua viagem é de {distancia}km e o valor da sua passagem ficou em R${preco:.2f}')