#                                             MÓDULOS E PACOTES

def factorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f
                               # Atenção: Essa aula é necessario colocar por modulos no templates olha a pasta 
                               # ( 22-Exemplo_Pratico)       essa atividade sera dividida em pastas diferentes.                         
def dobroo(n):                  # deixando o codigo menor e mais organizado quando for muito grande.
    return n * 2

def triploo(n):
    return n * 3


# Programa principal
num = int(input("Digite um valor: "))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}')