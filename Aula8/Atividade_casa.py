#Faça um programa que imprima os 10 primeiros números da sequência de fibonacci 

print("Sequência de fibonacci")
numero = int(input("Quantos termos você quer mostrar? "))
termo1 = 1
termo2 = 1
for i in range (numero):
    termo3 = termo1 + termo2
    print(f"{termo1}+{termo2}={termo3}")
    termo1 = termo2 
    termo2 = termo3



#Segunda opção de resultado
print("sequencia fibonacci")
numero = int(input("quantos termos? "))
termo1 = 1
termo2 = 1
fim = 0
while fim < numero:
    termo3 = termo1 + termo2
    print(f"{termo1}+{termo2}={termo3}")
    termo1 = termo2
    termo2 = termo3
    fim += 1
