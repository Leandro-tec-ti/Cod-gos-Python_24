# Refaça p desafio 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-='* 10)
primeiro = int(input("primeiro termo: "))
razao = int(input("Razãp da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    termo += razao
    print(f'{termo} --->>>')
    cont += 1
print("Fim")