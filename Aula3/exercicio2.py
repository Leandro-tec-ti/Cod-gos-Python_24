#identificando peso e altura do usuário
print("Sr. Leandro, gostariamos de saber qual é seu peso e altura? ")
peso = float(input("colocar seu peso "))
altura = float(input("colocar sua altura "))
imc = peso / (altura * altura)
print(f"O seu imc é {imc:.1f}")