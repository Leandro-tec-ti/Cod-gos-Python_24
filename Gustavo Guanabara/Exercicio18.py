# Exercicio 18
# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
#                   Para fazer esse tipo de questão sempre tem que utilizar "import math"
import math
angulo = int(input("Digite o ângulo que deseja: "))
seno = math.sin(math.radians(angulo)) #<<<--- Obs importante: primeiro precisar colocar o angulo para radianos e depois 
#converter para seno. Segue a formula  --->>>  seno = math.sin(math.radians(angulo))
print(f"O angulo de {angulo} tem o seno de {seno:.2f}")
cosseno = math.cos(math.radians(angulo)) # <<<---Obs importante: primeiro precisar colocar o angulo para radianos e depois 
#converter para cosseno. Segue a formula  --->>>  cosseno = math.cos(math.radians(angulo))
print(f"O angulo de {angulo} tem o cosseno {cosseno:.2f}")
tangente = math.tan(math.radians(angulo)) # <<<--- Obs importante: primeiro precisar colocar o angulo para radianos e depois 
#converter para tangente. Segue a formula  --->>>  tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem a tangente {tangente:.2f}')

#Segunda opção para desenvolver o calculo
from math import radians, sin, cos, tan  # <<<--- nessa resolução eu ja espefiquei qual metodo de calculo eu precisava
angulo = float(input("Digite o angulo que deseja: "))
seno = sin (radians(angulo))  # <<<--- ja que eu espqcifiquei, não preciso mais colocar math 
print(f'O angulo de {angulo}, tem o seno de {seno:.2f}')
cosseno = cos (radians(angulo))  # <<<--- ja que eu espqcifiquei, não preciso mais colocar math 
print(f'O angulo de {angulo}, tem o cosseno {cosseno:.2f}')
tangente = tan (radians(angulo))  # <<<--- ja que eu espqcifiquei, não preciso mais colocar math 
print(f'O angulo de {angulo}, tem a tangente {tangente:.2f}')