# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
while True:
    n = int(input('Digite um número: '))
# traduz: SE n NÃO TIVER NA LISTA números, ADCIONAR item DIGITADO PARA LISTA.
    if n not in numeros:
        numeros.append(n)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
print('=-'* 30)
numeros.sort() # <<<--- colocando os números em ordem crescente. 
print(f"Você digitou os valores {numeros}")