#faça um programa que peça 1 numero ao cliente e faça sua tabuada(até o 10)

x = 1
numero = int(input("Entre com um numero: "))
while x<11:
    multiplica = numero * x
    print(f"A multiplicação de {numero}x{x}={multiplica} ")
    x+=1
