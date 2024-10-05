# Faça um programa que pergunte quantos rodas tem um veículo
# Se tiver 4 rodas que é um carro ou van.

roda = int(input("Quantas Rodas tem seu carro? "))

if(roda==4):
    print("seu veiculo é um carro ou uma van ")
elif(roda == 2):
    print("O veiculo é uma moto ou bicicleta ")
elif(roda == 1):
    print("Este veiculo é um monocliclo ")
elif(roda == 6):
    print("esse veículo é um ônibus ")
elif(roda >=8 and roda<=20):
    print("Seu veículo provavelmente será um caminhão ")
else:
    print("seu Veiculo não foi encontrado com essa quantidade de rodas ")

