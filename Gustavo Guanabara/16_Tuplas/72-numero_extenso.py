# Crie um programa que tenha uma TUPLA totalmente preencheida com uma contagem por extenso, de zero a vinte.
# o programa deverá ler um número pelo teclado (entre 0 e 20 ) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')

print(f'Você Digitou o número {cont[num]}')