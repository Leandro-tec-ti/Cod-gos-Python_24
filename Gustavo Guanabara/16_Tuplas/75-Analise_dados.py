# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input('Digite 1° número: ')),
       int(input('Digite 2° número: ')),
       int(input('Digite 3° número: ')),
       int(input('Digite 4° número: ')))
print(f'Você digitou os valores {num} ')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado.')
print('Os números pares foram ', end='')
for n in num:  
    if n % 2 == 0: #<<<--- calculo para chegar aos número pares
        print(n, end=' ')
