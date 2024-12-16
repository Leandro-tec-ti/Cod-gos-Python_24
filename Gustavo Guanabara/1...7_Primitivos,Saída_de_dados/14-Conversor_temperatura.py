# Exercicio 14
#Faça um programa que converta uma temperatura digitada em °c(grau celsius) e converta para °f(grau fahrenheit)
c = float(input("Informe a temperatura em °C: "))
f = ((9 * c) / 5) + 32   # <<<--- Formula para converter de Celsius para Fahrenheit
print(f"A temperatura de {c}°C corresponde a {f}°F!")
