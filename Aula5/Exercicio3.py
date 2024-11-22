# Faça um programa para um lava rápido onde:
#1= Lavagem Completa a R$50,00
#2= Lavagem básica a R$35,00
# Caso o usuário queira, o pretinho custa mais R$ 5,00
#retorne o serviço + valor dele

nome = input("Qual é seu nome? ")
Lavarapido = int(input(f"Olá {nome} Seja bem vinda a nossa loja, temos opções para sua lavagem, escolha o que te atende: \n\n 1= Lavagem Completa a R$50,00  \n 2= Lavagem básica a R$35,00 ? \n"))

if(Lavarapido == 1):
    lavagem = "Lavagem Completa "
    valortotal = 50

elif(Lavarapido == 2):
    lavagem = "Lavagem Básica"
    valortotal = 35


pretinho = input("Sr. gostaria do pretinho no carro? ")

if pretinho == "sim":
    print("certo, terá um adccional de R$ 5,00 ")
    valortotal == valortotal + 5
elif pretinho == "não" or "nao":
    print(f"Valor total: {valortotal}")   
else:
    print(f"Ok! iremos fazer a sua lavagem solicitada. Valor Total ${valortotal}.")

print(f"O valor total do serviço é : {valortotal + 5. }")

