# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0,], [0, 0, 0,], [0, 0, 0,]]
soma_pares = maior = soma_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        #          soma dos pares
        if matriz[l][c] %2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é :{soma_pares}')
#         Soma da coluna
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma da coluna é : {soma_coluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
        