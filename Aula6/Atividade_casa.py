#Desenvolva um programa que simula um sistema de reciclagem com contagem dos materiais reciclado. Programa deve:
#Exibir uma mensagem de boas vindas ao usuario : "Bem vindo ao programa de reciclagem! ".

#solicitar ao usuario que informe o tipo de material que ele deseja reciclar, 
# entre vidro, metal, organico ou residuo não reciclavel.

#Com base no material informado, o programa deve informar a cor da lixeira correta para descarte e contabilizar
#a quantidade de cada matereial reciclado: 
#Papel: lixeira azul
#Plastico: lixeira vermelha
#Vidro: lixeira verde
#Metal: lixeira amarela
#Organico: lixeira marrom
#não reciclavel: lixeira cinza
#se nao for reconhecido, exibir a mensagem:"Erro tente novamente" não contabilizar na contagem de nenhuma lixeira.
#Perguntar ao usuario se ele deseja continuar reciclando. se o usuario digitar "s" 
#Programa deve repetir o processo; caso contrario o programa deve exibir um resumo da reciclagem
#com a quantidade de materiais reciclados e a mensagem : "Obrigado por contribuir com a Reciclagem "

jogador = input("Digite seu nome Jogador1? \n")
jogador2 = input("Digite seu nome jogador2? \n")
print(f"Bem vindo {jogador} e {jogador2} ao nosso jogo de reciclagem! \n")
print("Aquele jogador que fizer o maior números de pontos será o vencedor. \n")
print("Objetivo do jogo: recolher todo material reciclável e não reciclável, cada material recolhido tem uma pontuação diferente. \n")
print("O grande vencedor ganhará: UM PAR DE INGRESSO PARA O FILME CORINGA 2")
print("Regras do jogo: \n\n  1 = Papel: \n  2 = Plastico: \n  3 = Vidro: \n  4 = Metal: \n  5 = Organico: \n  6 = Não reciclavél: \n")

papel = 0 
papel1 = 0
plastico = 0
plastico1 = 0
vidro = 0
vidro1 = 0
metal = 0
metal1 = 0
organico = 0
organico1 = 0 
nao_reciclavel = 0
nao_reciclavel1 = 0
n2 = "sim"
while n2 == "sim":
#Jogador 1    
    n1 = int(input(f"{jogador}, quais são seu materiais a ser depositado? \n"))
    
    if(n1 == 1):
        print(" Você ganhou 5 pontos ")
        papel = papel + 5
    elif(n1 == 2):
        print(" Você ganhou 5 pontos ")
        plastico = plastico + 5
    elif(n1 == 3):
        print("Você ganhou 5 pontos ")
        vidro = vidro + 5
    elif(n1 == 4):
        print(" Você ganhou 7 pontos ")
        metal = metal + 7
    elif(n1 == 5):
        print(" Você ganhou 10 pontos ")
        organico = organico + 10
    elif(n1 == 6):
        print(" Você ganhou 10 pontos ")
        nao_reciclavel = nao_reciclavel + 10
    else:
        print("Erro tente novamente ")
#Jogador 2
    n2 = int(input(f"{jogador2}, quais são seus materiais a ser depositado? \n"))
    if(n2 == 1):
            print(" Você ganhou 5 pontos ")
            papel1 = papel1 + 5
    elif(n2 == 2):
        print(" Você ganhou 5 pontos ")
        plastico1 = plastico1 + 5
    elif(n2 == 3):
        print(" Você ganhou 5 pontos ")
        vidro1 = vidro1 + 5
    elif(n2 == 4):
        print(" Você ganhou 7 pontos ")
        metal1 = metal1 + 7
    elif(n2 == 5):
        print(" Você ganhou 10 pontos ")
        organico1 = organico1 + 10
    elif(n2 == 6):
        print(" Você ganhou 10 pontos ")
        nao_reciclavel1 = nao_reciclavel1 + 10
    else:
        print("Erro tente novamente ")
    n2 = input(f"Outra rodada? sim ou nao \n").lower()
print(f"O resultado da reciclagem do Jogador 1 foi:\n Papel:{papel}\n Plástico:{plastico}\n Vidro:{vidro}\n Metal:{metal}\n Organico:{organico}\n não reciclavél:{nao_reciclavel}\n ")
total1 = papel + plastico + vidro + metal + organico + nao_reciclavel
print(f"{total1}")
print(f"O resultado da reciclagem do Jogador 2 foi:\n Papel:{papel1}\n Plástico:{plastico1}\n Vidro:{vidro1}\n Metal:{metal1}\n Organico:{organico1}\n não reciclavél:{nao_reciclavel1}\n ")
total2 = papel1 + plastico1 + vidro1 + metal1 + organico1 + nao_reciclavel1
print(f"{total2}")
if (total1 > total2):
    print(f" O vencedor é o jogador: {jogador} ")
else:
    print(f" O vencedor é o jogador: {jogador2} ")