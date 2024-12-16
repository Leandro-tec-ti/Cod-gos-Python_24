for c in range(0,6): # <<<--- Ele repediu o Olá mundo 6X
    print("Olá Mundo! ")
print("Fim ")

for c in range(6, 0, -1):  #<<<--- Contagem regressiva é necessário colocar o "-1" no final
    print(c)
print("Fim")

for c in range(0, 7, 2):#<<<--- esse "2" faz o algoritimo contar de 2 em 2 / se colcocar "3" vai contar de 3 em 3 e assim...
    print(c)
print("Fim")

n = int(input("digite um numero: "))
for c in range(0, n+1):#<<<--- esse "+1" é para finalizar no numero que usuário digitou
    print(c)
print("Fim ")

n = int(input("digite um numero: "))
for c in range( n, 0, -1):#<<<--- esse "n" foi criado um input para que o usuário digite qualquer número
    print(c)
print("Fim ")

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):#<<<-- Também pode-se colocar letras dentro do Range
    print(c)
print("Fim")
s = 0  #<<< importante no for colocar uma variante recebendo "0"
for c in range(0, 3): #<<<--- pode colocar Frases ou input para repetir varias vezes
    n = int(input("Digite um valor: "))
    s += n  # Aqui o for pode fazer o calcule da quantidade de numeros que coloquei
print(f"A soma foi {s} ")
