# Exercicio 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.
import random # <<<--- Aqui não especifiquei o metodo, entao ele carrega toda a biblioteca random
n1 = str(input("Primeiro aluno: "))
n2 = str(input('Segundo aluno: '))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4] # <<<--- para montar uma lista no python é necessario esta entre conchetes "[]"
escolhido = random.choice(lista) # <<<--- uma escolha dentro da lista já definida
print(f"O aluno escolho foi: {escolhido}")

#Segunda forma de desenvolver o programa
from random import choice # <<<--- Aqui eu especifiquei o metado de escolha (choice)
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista) # <<<--- não é necessario colocar random. pq ja espefiquei lá em cima no inicio do Exercicio
print(f'O aluno escolhido foi: {escolhido}')