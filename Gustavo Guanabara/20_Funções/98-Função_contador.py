# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def linha():
    print('=-' * 30)


def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

linha()
def contador(i, f, p):
    print(f' Contagem de {i} até {f} de {p} em {p} ')

    if p < 0 :
        p *= -1
    if p == 0 :
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)#<<-- "flush=True" é para parar a contagem toda de uma vez, e contar 1 á 1
            sleep(0.5)
            cont += p
        print(' FIM! ')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print(' FIM ')


# programa principal
contador(1, 10, 1)
linha()
contador(10, 0, 2)

escreva('  Agora é sua vez de personalizar a contagem  ')

inicio = int(input('Qual o numero inicial da contagem? ==> '))
fim = int(input('Qual é ultimo número da contagem? ==> '))
passo = int(input('De quanto em quanto vc quer contar? ==> '))
contador(inicio, fim, passo)