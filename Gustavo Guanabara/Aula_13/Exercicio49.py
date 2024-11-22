# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um for.

s = 0
for c in range(0, 10):
    n = int(input("Digite seu numero: "))
    print(f"{n} x {1} = {n*1} ")
    