#faça 
resultado = 0
for i in range(4):
    n = int(input("Digite seu numero: "))
    if n % 2 != 0:
        resultado +=n
print(f"O resultado da soma é : {resultado}")
