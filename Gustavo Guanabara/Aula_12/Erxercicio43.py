# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condiçôes de pagamento:
# À VISTA (dinheiro / cheque): 10% de desconto
# À VISTA ( cartão): 5% de desconto
# 2x no cartão : preço normal
# 3x ou mais no cartão : 20% de juros

print('Super Mercado')

preco = float(input('Preço das compras: '))
print('''Formas de pagamento 
[1] À vista dinheiro / cheque
[2] À vista cartão Débito
[3]  até 2x no cartão Crédito
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua opção de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)#<<<--- o que está entre parenteses é a formula para calcular a porcentagem
    print(f'Pagando dessa forma você terá 10% de desconto na sua compra, novo valor ficou em R${total:.2f} ')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Pagando dessa forma você terá 5% de desconto na sua compra, novo valor ficou em R${total:.2f} ')
elif opcao == 3:
    print(f'O valor ficou em R${preco:.2f} ')
    forma = int(input('Quantas vezes deseja pagar Crédito à vista ou em 2X?\n [1] 1 vez\n [2] 2 vezes '))
    if forma == 1:
        print(f'Ficou 1 vez de R${preco:.2f}')
    elif forma == 2:
        parcela = preco / 2
        print(f'A parcela ficou em R${parcela:.2f}')
else:
    forma = int(input('Quantas vezes deseja parcela suas compras?\n [1] 3X\n [2] 4X\n [3] 5X '))

    if forma == 1:
        print
    elif forma == 2:
        print
    else:
        print

