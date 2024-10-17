import random

#Gera um numero inteiro aleatorio entre 1 a 100
numero_aleatorio = random.randint(1, 100)
print(f"numero inteiro aleatorio entre 1 a 100: {numero_aleatorio}")


#Obervação:  Em funções passamos parametros (numero, variaveis). muitas vezes não temos acesso a lógica por trás.
#eles servem para facilitar o desenvolvimento e evitar codigos desnecessarios ou "re-invenção da roda".
#bibloteca costumam ter varias funções.

print("Entre com dois numeros, irei retorno um numero aleatório entre eles ")
num_menor = int(input("Entre com o menor numero: "))
num_maior = int(input("Entre com o numero maior: "))
numero_aleatorio2 = random.randint(num_menor, num_maior)

print(f"Numero inteiro aleatorio entre {num_menor} e {num_maior}: {numero_aleatorio2}")

