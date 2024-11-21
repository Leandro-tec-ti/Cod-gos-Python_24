# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar
#  o valor da casa e o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode excerder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Quantos anos pretende pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação ficou de R${prestacao:.2f}')
if prestacao <= minimo:
    print("Empréstimo liberado ")
else:
    print('Empréstimo negado ')