numero = int(input("Digite um numero: "))

#saber se um numero é divisível por 3 
if((numero % 3 ) == 0):
    print("Este numero é divisível por 3 ")
    if numero %5 == 0:
        print("o numero é divisível por 5 ")
elif numero % 5 == 0:
    print("este numero é divisivel por 5")
else:
    print("este numero não é divisível por 5 ")