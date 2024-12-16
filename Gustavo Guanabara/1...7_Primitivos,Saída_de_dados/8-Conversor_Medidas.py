#exercicio 8
#Faça um programa que leia um valor em metros e exiba convertido em centimetros e milimetros 
#Segunda parte do Exercicio, converta metros em dam; hm. e km. no mesmo exercicio.
m = float(input(" Quantos metros vc deseja? "))
cm = m * 100
mm = m * 1000
dam = m / 100
hm = m / 500
km = m / 1000
print(f"{m}, correspondem a :{cm} Centimetros, {mm} milimetros. \n Em decametro{dam}, hecametro{hm}, e kilometro{km} ")

