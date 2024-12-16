# Refaça o dessafio 035 dos triângulos, acrescentando p recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lasod iguais
# Isósceles: dois lados iguais
# Escaleno: Todos os lados diferentes

r1 = int(input('Digite o primeira reta '))
r2 = int(input('Digite o segunda reta '))
r3 = int(input('Digite o terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3: #<<<--- if dentro de if 
        print("Equilátero")
    elif r1 != r2 != r3 != r1:
        print('Escaleno ')
    else:
        print('Isósceles')
else:
    print('As retas acima não podem formar um triângulo')

