#faça um programa que peça ao usuário para inserir 5 números.
#o programa deve calcular a soma acumulada desses números e exibir o resultado final.

#Peça ao usuário para inserir 5 numeros. 
#Requisito: use uma variavél acumuladora para armazenar a soma dos numeros. 
#após o usuario inserir todos os numeros, exiba a soma total:

print("Olá usuário digite 5 números ")

acumuladora = int(input("digite um numero "))
acumuladora = acumuladora + int(input("digite outro numero "))
acumuladora = acumuladora + int(input("digite outro numero "))
acumuladora = acumuladora + int(input("digite outro numero "))
acumuladora = acumuladora + int(input("digite mais um numero "))
print(f" resultado é: {acumuladora}")