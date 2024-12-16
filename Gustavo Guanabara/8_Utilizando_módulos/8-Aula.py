# Aula 8 (Gustavo Guanabara)
# Apredendo Módulos 
#EX: identificando a Rais quadrada
import math # <<<--- com essa função eu faço o carregamento da biclioteca inteira com todos os metodos matemáticos 
num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print(f"raiz de {num} é igual a {raiz:.2f} ")

#Segunda opção de para execução da atividade
from math import sqrt # <<<--- nesta função eu especifico metodo matemático que quero para o projeto.
num = int(input("Digite um numero? "))
raiz = sqrt(num) # <<<--- Aqui eu não preciso mais espeficicar o metodo
print(f"A raiz do {num} é igual a {raiz:.2f}")

#Terceira opção de execução para utilizar mais de uma função no mesmo trabalho
from math import sqrt, floor
num = int(input("Digite um numero? "))
raiz = sqrt(num)
print(f"A raiz de {num} é igual a {floor(raiz)}")

