#Função: calcule o quadrado de um numero


def quadrado(numero):
    return numero ** 2

numero = float(input("digite um numero: "))
resultado = quadrado(numero)    #<<<--- recebe o retorno da função
print(f"O quadrado de {numero} é {resultado}")

#código principal: pode chamar