# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista_numero = []
maior = 0
menor = 0

for c in range(0, 5):
   lista_numero.append(int(input(f'Digite um valor para a posição {c}: ')))
   # Estrutura de código para saber qual é o mair Valor e qual é o menor Valor
   if c == 0:
      maior = menor = lista_numero[c]
   else:
        if lista_numero[c] > maior:
         maior = lista_numero[c]
        if lista_numero[c] < menor:
           menor = lista_numero[c]
           
print('=-'* 30)
print(f'Você digitou os valores {lista_numero}')
print(f'Maior número digitado foi:{maior} nas posições ', end='')
for i , v in enumerate(lista_numero):
   if v == maior:
      print(f'{i}... ', end='')
print()

print(f'Menor número digitado foi: {menor} nas posições ', end='')
for i , v in enumerate(lista_numero):
   if v == menor:
      print(f'{i}... ', end='')
print()