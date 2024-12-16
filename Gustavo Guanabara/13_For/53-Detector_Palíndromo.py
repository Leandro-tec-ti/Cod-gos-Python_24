# Crie um programa que leia uma frase quelquer e diga se ela é um Políndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper() # ".strip()" para retiras espaços vazios externos
#                                                          "upper()"  para deixar as letras maiuscula

palavras = frase.split()  # <<<---  "split()" divide cada palavras do texto 
junto = '' .join(palavras)  #<<<--- ".join()" Vai juntar o texto e deixar sem espaços.  
inverso = ''
for letra in range(len(junto) - 1 ,- 1, -1): #<<--O último "-1" ele serve para comecar a leitura ou contagem do lado contrario
    inverso += junto[letra]
print(f"\nVocê digitou a frase:{junto}\n e a frase inverso: {inverso}\n ")
if inverso == junto:
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")


