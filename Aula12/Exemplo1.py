# Definindo uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

#acessando uma linha inteira
print("segunda linha da matriz:", matriz[1])

#acessando elemento especificos
print("elemento da terceira linha e primeira coluna", matriz[2][0])

#acessando o elemento na 2° linha e na 3° coluna
elemento = matriz[1][2]
print(elemento)

#matriz no python funciona como um conjunto de listas/vetoris;
#pense como um armario com varias gavetas
#            0   1   2    3   4    <<<--- linha de contagem
#         0 [  ][  ][  ][  ]
#         1 [  ][  ][  ]  
#         2 [  ][  ][  ][  ][  ]
#         3 [  ][  ][  ][  ][  ]
#         ^--------------- coluna de contagem

