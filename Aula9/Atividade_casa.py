#Adicione ao jogo da adivinhação a opção de colocar 1 ou 2 números para serem advinhados simultaneamente
import random 
#numero1 = random.randint(1, 100)
#numero2 = random.randint(1, 100)
#print(f"{numero1} e {numero2}")
#quant = input("Deseja advinha 1 ou 2 numeros? ")
#if quant == "1":
#    for i in range(5):
#        palpite = int(input("Digite seu palpite: "))
#        if palpite == numero1:
#            print("Parabens, voce acertou")
#            break
#        elif palpite < numero1:
#            print("O numero é maior!")
#        else:
#            print("O numero é menor!")
#    else:
#        print(f"infelizmente não foi dessa vez, os  numeros foram: {numero1}, tente novamente")        
#elif quant == "2":
#    for i in range(5):
#        palpite = int(input("Digite seu palpite: "))
#        if palpite == numero1 or palpite == numero2:
#            print("Parabens, voce acertou")
#            break
#        elif palpite < numero1 or palpite < numero2:
#            print("O numero é maior!")
#        else:
#            print("O numero é menor!")         
#    else:
#        print(f"infelizmente não foi dessa vez, os  numeros foram: {numero1} e {numero2}, tente novamente")

#Segunda alternativa de programa

numero1 = random.randint(1, 100)
numero2 = 0
quant = input("Deseja adcionar mais um numero para tenta a sorte? s / n ")

if quant == "s":
    numero2 = random.randint(1, 100)
print(f"{numero1} e {numero2}")
for i in range(5):
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero1: 
        print("Parabens você acertou!")
        break
    elif numero2 > 0:
        if palpite == numero2:
            print("Parabens você acertou!")
            break
        else:
            if(palpite < numero1):
                print("O primeiro numero é maior!") 
            else:
                print("O primeiro numero é menor!") 
            if(palpite < numero2):
                print("O segundo numero é maior!") 
            else:
                print("O segundo numero é menor!") 
    else:
        if(palpite < numero1):
            print("O numero é maior!") 
        else:
            print("O numero é menor!") 
