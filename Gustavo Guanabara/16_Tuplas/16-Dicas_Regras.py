# Regras e Dicas para Tuplas

# ATENÇÃO: TUPLA É IMUTÁVEIS (não pode ser trocados)

lanche = 'hamburguer', 'suco', 'pizza', 'pudinm'
#              [0]       [1]      [2]       [3]
#              [-4]      [-3]     [-2]      [-1]   <<<--- lista de forma reversa

print(lanche)
print(lanche[2])# <<<--- posso adcionar "[]" para saber qual item da lista de lanche eu quero
print(lanche[-3])# <<<---  dessa forma eu estou colocando em lista reversa "ao contrário"
print(lanche[1:3])#<<-- Estou desejando alguns itens da lista, só o 1 e 2 que é 'suco' e 'pizza.
print(lanche [1:])# estou iniciando no numero um dá lista e indo até o final 
print(lanche[:2])# estou finalizando no numero 2, ou seja ele vai trazer todos itens da lista até numero 1.
print(lanche[-3:])# com a lista reversa ele vai me trazer do -3 até o final  (suco, pizza, pudim)
print(sorted(lanche))# o "sorted" é para colocar em ordem Alfabética dentro da lista.

# 1° maneira de fazer for com TUPLAS  
for comida in lanche:
    print(f'Eu vou comer {comida}')

# 2° maneira de fazer for com TUPLAS 
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {comida} na posição {cont}')

#3° maneira de fazer for com TUPLAS 
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')