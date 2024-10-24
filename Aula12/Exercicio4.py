#Após a aventura da aula passada, o aventureiro resolveu treinar mais seu combate: Faça uma simulaçao onde o aventureiro tem uma lsita [100, 20],
#onde 100 é a vida dele e 20 é o poder de ataque dele e a cada 7 segunsdos de treino, ele aumenta o seu poder de ataque e 1 e o limite maximo de 30, para seu poder de ataque.

#import time
#print("Olá aventureiro, iremos inciar seu treinamento")
#print([100, 20])
#vida = 100
#poder = 20

#contador = 20

#while contador <= 29:
   # print(contador)
  #  time.sleep(0)
  #  contador += 1
 #   print(f"depois do treino seu poder foi:{contador}")
#print(f"seu poder depois do treinamento foi para:{contador}")

# segunda Altenativa

#Exercicio de treinamento do aventureiro:
import time
aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
for linha in aventureiro:
    print(linha)
print("o treino começou!")
while  aventureiro[1][1] < 30:
    aventureiro[1][1] += 1
    print("o poder de ataque atual é", aventureiro[1][1])
    time.sleep(3)
print("Status final:")
for linha in aventureiro:
    print(linha)


        


