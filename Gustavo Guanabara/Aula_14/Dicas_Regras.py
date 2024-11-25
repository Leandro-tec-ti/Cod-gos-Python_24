#  Dicas e Regras

###while é para quando vc não sabe quantos passos é nessesario para chegar ao limite. 
# ele irá ficar repedindo ate chegar ao um limitador
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print("Fim")'''

r = "s"
while r == "s": #<<<--- Enquanto isso for verdadeiro vai ficar rodando
    n = int(input("Digite um numero: "))
    r = str(input("Quer continuar? [S/N] ")).lower()
print("Fim")

n = 1 
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} pares, e digitou {impar} impares")