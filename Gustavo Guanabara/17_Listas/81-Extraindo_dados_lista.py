#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    
    print('Seu número foi adcionado com sucesso ')
    
    lista.sort(reverse=True)

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
print(f'foram digitados {len(lista)} números, a sua lista ficou {lista} ')
# se 5 está na lista. (traduzindo esse if)
if 5 in lista:
    print('o valor 5 faz parte da Lista.')
else:
    print('o Valor 5 não esta na lista.')