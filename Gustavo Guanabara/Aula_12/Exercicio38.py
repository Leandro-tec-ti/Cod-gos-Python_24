# Escreva um  programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
# o Primeiro valor é maior
# o Segundo valor é maior
# Não existe valor maior, os dois são iguais

valor1 = int(input('Digite seu Primeiro Valor: '))
valor2 = int(input('Digite seu segundo Valor: '))
if valor1 > valor2:
    print(f" O primeito valor {valor1} é maior que o segundo valor {valor2}")
elif valor1 < valor2:
    print (f'O segundo Valor {valor2} é maior que o primeiro valor {valor1}')
else:
    print(f"Os valores {valor1} e o {valor2} são iguais! ")