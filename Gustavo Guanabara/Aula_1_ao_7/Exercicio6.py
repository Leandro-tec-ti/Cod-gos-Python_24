#Exercicio 6
#faça um programa que crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input(" Digite seu numero: "))
d = n * 2
t = n * 3
r = n ** (1/2) # --->>> essa é a formula para calcular a Raiz quadrada de algum número 
print(f"O numero digitado foi:{n}, e o seu dobro é:{d}, seu triplo é:{t}, e sua raiz quadrada é:{r} ")