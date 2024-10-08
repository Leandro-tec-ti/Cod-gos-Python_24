# Faça um programa que: perguente se o usuário quer um combo ou um item individual.
#Hamburgue: R$ 10,00
#Batata Frita: R$ 10,00
#Refrigante: R$ 10,00
#Combo custa: R$ 22,00

nome = input("Qual é seu nome? ")
valor = int(input(f"Olá {nome }, seja bem vindo a nossa Lanchonete, temos algumas opções de lanche, São elas: \n \n 1 = Hamburgue: R$ 10,00  \n 2 = Batata Frita: R$ 10,00  \n 3 = Refrigante: R$ 10,00\n\n "))


if(valor == 1):
    lanche = "Hamburguer "
    Extra = 10.00
    
elif(valor == 2):
    lanche = "Batata Frita "
    Extra = 10.00

elif(valor == 3):
    lanche = "Refrigerante "
    Extra = 10.00
    
    #saber se o cliente irá querer mais um lanche
extra = input(f"Sr. seu pedido escolhido foi {lanche}. Gostaria de uma Segunda opção de lanche? \n ")


if extra == "sim" :
    print("Certo, daremos continuidade. \n ")


else:
    print("ok! faremos seu pedido ")

    #oferecendo o lanche

kit = int(input("\n Qual seria o segundo item? \n "))


if(kit == 1):
    lanche1 = "Hamburguer "

elif(kit == 2):
    lanche1 = "Batata frita "

elif(kit == 3):
    lanche1 = "Refrigerante "

extra2 = input(f" seu pedido é {lanche1} com {lanche} seu pedido total esta dando R${Extra + Extra} \n Por apenas R$2.00 poderá levar um Combo com todos os itens, gostaria de aproveitar? \n")


if extra2 == "sim":
    print(" seu pedido será feito, valor total do pedido é de R$ 22.00 \n")

else:
    print(f" Seu pedido será feito, valor total do pedido é R${Extra + Extra} ")

