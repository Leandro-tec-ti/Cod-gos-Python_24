# EXERCICIO 5
#faça um  programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
n1 = int(input("Digite um numero: "))
a = n1 - 1
s = n1 + 1
print(f"Analisando seu numero:{n1}, seu antecessor é :{a}, e o seu sucessor é:{s} ")
#segunda opção é:
print(f"Analisando seu numero:{n1}, seu antecessor é :{n1-1}, e o seu sucessor é:{n1+1} ") #E elimina as variáveis "a" e "s".