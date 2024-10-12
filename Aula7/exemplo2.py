# Gerar numeros de 2 a 6 (7 não é incluído):
n1 = int(input("digite um numero:"))
#uso uma variavél de apoio que definira se em numero é primo ou não
primo = True
#faça um loop que vai do numero 2 até o numero antecessora ele
for i in range(2, n1):
    #se um numero for divisivel por qualquer numero sem ser 1 ou ele mesmo, primo será falso
    if(n1%i==0):
        primo = False
        #se um numero for divisivel por qualquer numero por mais algum sem ser 1 e ele mesmo
if(primo == False):
    print("Esse numero não é primo ")
else:
   print("esse numero é primo ")