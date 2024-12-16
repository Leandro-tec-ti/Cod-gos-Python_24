# Exercicio 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random #<<<--- importei toda a biblioteca de random 
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista) #<<<--- Espefifiquei qual metodo quero utilizar para a questão (shuffle = embaralhar)
print(f'A ordem de apresentação será:{lista}')

#Segunda Alternativa resolução
# obs: quando for especificar o metodo no inicio, sempre colocar "from" primeiro e "import" sempre será a terceira palavra.
from random import shuffle #<<<--- espefiquei o metodo no inicio 
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1, n2, n3, n4]
shuffle(lista)   # <<<--- Especifiquei o metado no inicio, não devo utilizar o random nesta porte do exercicio.
print(f"A ordem de apresentação será: \n{lista}")