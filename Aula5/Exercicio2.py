# Faça um programa que: perguente se o usuário quer um combo ou um item individual.
#Hamburgue: R$ 10,00
#Batata Frita: R$ 10,00
#Refrigante: R$ 10,00
#Combo custa: R$ 22,00

valor = int(input("Olá cliente, seja bem vindo a nossa Lanchonete, temos algumas opções de lanche, São elas: \n \n 1 = Hamburgue: R$ 10,00  \n 2 = Batata Frita: R$ 10,00  \n 3 = Refrigante: R$ 10,00\n\n "))

if(valor == 1):
    lanche = "Hamburguer "

elif(valor == 2):
    lanche = "Batata Frita "

elif(valor == 3):
    lanche = "Refrigerante "
    
    #saber se o cliente irá querer mais um lanche
lanche1 = int(input("Sr. Gostaria de uma Segunda opção de lanche? \n\n 1= sim \n 2= não "))

if(lanche1 == 1):
    print("Qual seria a segunda opção?")

elif(lanche1 == 2):
    print("Ok! Faremos seu Pedido. ")

else:
    print("Esta opção é inválida! ")

    #oferecendo o lanche

kit = input(" Temos uma grande promoção, gostaria de aproveitar? \n \n COMBO PROMOCIONAL: \n Por apenas R$ 22,00 ") 
