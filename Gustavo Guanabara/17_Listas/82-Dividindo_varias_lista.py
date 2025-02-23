#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
# for 'i' é índice, 'v' é número digitado, 'enumerate' vai numerar pra mim o valor digitado pelo usuário 
for i, v in enumerate(lista):
    if v %2  == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'Lista total: {lista}, lista pares: {par}, lista ímapres:{impar}')