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
numero = int(input("quantos termos você quer mostrar? "))
termo1 = 1
termo2 = 1
fim = 0
while fim < numero:
    termo3 = termo1 + termo2
    print(f"{termo1}+{termo2}={termo3}")
    termo1 = termo2
    termo2 = termo3
    fim += 1

#                    precisar entender o raciocionio 
#Terceira opção de resultado
a = 1
b = 1
pulo = 1
for i in range(10):
    print(a)
    pulo = b - a # <<<--- Atualiza "plulo" com a distancia entre os numeros
    temp  = a    # <<<--- Armazena o valor atual de "a" em variavel temporária
    a = b        # <<<--- Atualiza "a" com valor de "b"
    b = temp + b # <<<--- atualiza "b" com a soma do antigo "a" e "b"
