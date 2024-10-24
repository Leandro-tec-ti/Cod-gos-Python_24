#Faça um programa que simule o armario de uma escola e permita colocar o nome do aluno resposável pagante da gaveta. o armario tem a dimensão 5x5

matriz = [
    ["1","2","3","4","5"],
    ['6','7','8','9','10'],
    ["11","12","13","14","15"],
    ['16','17','18','19','20'],
    ['21','22','23','24','25']
]

nome = input("qual é seu nome \n")
linha = int(input("Em qual linha do armario será a sa gaveta: (0 a 4) \n"))
coluna = int(input("qual é a coluna do armario será a sua gaveta? (0 a 4) \n"))
matriz[linha][coluna] = nome

for linha in matriz:
    print(linha)



