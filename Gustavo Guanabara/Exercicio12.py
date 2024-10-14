#Exercicio 12
#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#complemento ao exercicio, pergunte ao cliente qual é a % de desconto?
valor = float(input("Qual é o valor do produto? "))
porc = float(input("Quantos % é o seu desconto? "))# <<<--- observação: atividade extra (complemento)
resul = valor * porc / 100 #<<<--- observação: atividade extra (complemento)
real = valor - resul
print(f"O Valor do seu produto com desconto é: {real:.2f}R$ ")

#Segunda opção para Calcular de forma mais otimidada colocar entre "()" o calculo
#resul = valor - (valor * 5 / 100)
#print(f"O Valor do seu produto com desconto de: {resul:.2f}R$ ")