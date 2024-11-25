# Crie um programa que leia dois valores e mostre um menu como abaixo na tela:
# Seu programa deverá realizar a operação solicitada em cada caso.
# []Somar
# []Multiplicar
# []Maior
# []Novos números
# []Sair do programa
from time import sleep
numero1 = int(input("Primeiro Valor: "))
numero2 = int(input("Segundo Valo: "))
opcao = 0
while opcao != 5:  #<<<--- enquanto a resposta não for 5 o programa ira ficar perguntando.
    print('''
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa''')
    opcao = int(input("Qual é a sua opção? "))
# Aqui estou somando
    if opcao == 1:
        total = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é {total}")
# Aqui estou multiplicando
    elif opcao == 2:
        total = numero1 * numero2
        print(f"A multiplicação de {numero1} e {numero2} é {total}")
# Aqui estou identificando o maior numero
    elif opcao == 3:
        if  numero1 < numero2:
            print("Primeiro numero é menor e Segundo numero é maior")
        if  numero2 < numero1:
            print("Segundo numero é menor e o primeiro numero é maior")
# Aqui estou Reiniciando
    elif opcao == 4:
        print("Reiniciando... ")
        sleep(1)
        numero1 = int(input("Primeiro Valor: ")) #<<<--Obs: para reiniciar preciso solicitar ao usuário a pergunta incial
        numero2 = int(input("Segundo Valo: "))
# Aqui estou finalizando
    elif opcao == 5:
        print("Encerrado! ")
    else:
        print("Opçãp invalida: ")
print("Fim")
