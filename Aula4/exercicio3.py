# Faça um programa calcule o IMC do usuário e de classificação conforme a tabela ao lado:
# calculo do IMC :     imc = peso/altura*altura

peso = float(input("Qual é seu peso? "))
altura = float(input("qual é sua altura? "))
imc = peso / (altura*altura)

if(imc <18.5):
    print(f"magreza seu imc é : {imc:.1f}grau = 0")  
elif(imc <25 ):
    print(f"normal seu imc é.: {imc:.1f} grau = 0 ") 
elif(imc <30):
    print(f"sobrepeso seu imc é : {imc:.1f} grau = 1 ") 
elif(imc <40):
    print(f"obesidade seu imc é : {imc:.1f} grau = 2")
else:
    print(f"obesidade grave seu imc é : {imc:.1f} e o grau da obesidade é grau 3")
    





