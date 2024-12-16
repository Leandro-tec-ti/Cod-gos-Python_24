# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um for.

n = int(input("Digite seu numero: "))
for c in range(1, 11):
    print(f"{n} x {c} = {n*c} ")
    