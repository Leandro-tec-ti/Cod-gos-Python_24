# Faça um programa que tenha uma função chamada converter. Essa função deve receber uma temperatura em celcius e retorna fahrentit

c = float(input("Informe a temperatura em °C: "))
f = ((9 * c) / 5) + 32   # <<<--- Formula para converter de Celsius para Fahrenheit
print(f"A temperatura de {c}°C corresponde a {f}°F!")





#segunda Alternativa

def quadrado(numero):
    return numero * 9 / 5 + 32

c = float(input("digite um numero: "))
resultado = quadrado(c)    #<<<--- recebe o retorno da função
print(f"O quadrado de {c} é {resultado}")