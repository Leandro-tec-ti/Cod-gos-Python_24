# Faça um programa que conte de 0 a 10 e diga no final "obrigado por esperar! estamos redirecionando sua ligação."

import time
print("iniciando contagem ")
contador = 5

while contador < 10:
    print(contador)
    time.sleep(1)
    contador += 1
print("Obrigado por esperar! estamos redirecionando sua ligação ")
