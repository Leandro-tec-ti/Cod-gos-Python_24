#Exercicio 11
#Faça um programa que leia uma largura e uma altura de uma parede em metros, calcule a sua area e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input("Qual é a largura da parede? "))
alt = float(input("Qual é a Altura da parede? "))
area = larg * alt   # --->>> formula para calcular m² de uma area
print(f"Sua parede tem {larg}x{alt} e tem {area:.2f}m² ")
tinta = area / 2
print(f"Para pinta essa parede, você irá precisar de {tinta:.2f}l de tinta.")