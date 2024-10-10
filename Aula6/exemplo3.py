#Faça um programa que some infinitamente numeros que o usuario coloca e só pare de somar caso  ele solicite

x = True
soma = 0
while (x==True):
    numero = float(input("Digite um numero:"))
    continuar = input("Continuar ou parar?").lower()
    if (continuar == "parar"):
        soma += numero
        print(f"a soma deu {soma}")
        x=False
    else:
        soma += numero

