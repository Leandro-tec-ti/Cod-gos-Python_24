# 
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break  # <<<--- Break é para finalizar o while quando ele for infinito.
    s += n
print (f"A soma vale {s}")