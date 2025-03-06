# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def linha():
    print('<-' * 40)


def area(largura, cumprimento):
    m = largura * cumprimento
    print(f'A área de um terreno {largura} x {cumprimento} é de {m}m²')

# Programa principal
linha()
print('  Dimensões de Terreno  ')
linha()
largura = float(input('Largura do terreno (m) ==> '))
cumprimento = float(input('Cumprimento do terreno (m) ==> '))
area(largura, cumprimento)