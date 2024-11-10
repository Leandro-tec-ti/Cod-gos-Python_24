# Exercicio 13
#Faça um algoritimo que leia o Salario de um Funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input("Qual é seu salario atual? "))
atual = salario + (salario * 15 / 100)
print(f"Seu novo salario teve um reajuste com uma valorização com 15%, seu valor atual foi para: {atual:.3f}")