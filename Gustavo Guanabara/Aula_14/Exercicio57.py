# Faça um programa que leia o sexto de uma pessoa, mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente até ter um Valor correto.


sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
idade = int(input("Agora Informe sua idade: "))
while sexo not in "MF":
    sexo = str(input("Dados invalidos. Digite o sexo correto: "))
print(f"Sexo {sexo} Registrado com sucesso! ")