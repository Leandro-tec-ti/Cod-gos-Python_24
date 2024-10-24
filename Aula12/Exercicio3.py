#Faça um programa que simule o armario de uma escola e permita colocar o nome do aluno resposável pagante da gaveta. o armario tem a dimensão 5x5
#A escola adicionou um novo armario 3 x 3 perto da salas de aula e o chamou de armario vip. caso o aluno adquira uma gaveta no armario comum, 
#custará R$: 30.00 ao mes. o vip custará R$: 50 reais. adcione no sistema essa seleção e retorne para o usuario o custo:

matriz = [
    ["1","2","3","4","5"],
    ['6','7','8','9','10'],
    ["11","12","13","14","15"],
    ['16','17','18','19','20'],
    ['21','22','23','24','25']
]

matriz2 = [
    ['','',''],
    ['','',''],
    ['','','']
]

nome = input("qual é seu nome \n")
print("Temos armario tem o beneficio de esta mais proximo da sala de aula: S / N \n armario comum: 30,00 \n armario vip: 50,00")
pergunta = input(f"{nome} Gostaria de aproveitar nosso Armario vip? \n ")
if pergunta == "s":
    
    linha = int(input("Em qual linha do armario será a sa gaveta: (0 a 2) \n"))
    coluna = int(input("qual é a coluna do armario será a sua gaveta? (0 a 2) \n"))
    matriz2[linha][coluna] = nome
    for linha in matriz2:
     print(linha)
    print("O valor ficou de 50,00 reais")
elif pergunta == "n":
    print("Temos uma segunda opção de armario um pouco mais longe da sala")
    
    linha = int(input("Em qual linha do armario será a sa gaveta: (0 a 4) \n"))
    coluna = int(input("qual é a coluna do armario será a sua gaveta? (0 a 4) \n"))
    matriz[linha][coluna] = nome
    for linha in matriz:
     print(linha)
    print("O valor ficou de 30,00 reais")
else:
    print("certo, aproveite a nossa escola! ")


