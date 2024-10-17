
print("Queremos saber a sua resposta")
ponto1 = 0
ponto2 = 0
ponto3 = 0
joga = "sim"
while(joga == "sim"):
    perg1 = input("1 + 1 é 2 como resultado?  ")
    if (perg1 == "sim"):
        print("Parabéns acertou")
        ponto1 += 1
    else:
        print("Tente novamente")
    perg2 = input("2 + 2 é 5 como resultado? ")
    if(perg2 == "sim"):
        print("Você errou")
    else:
        print("Paraben acertou")
    ponto2 += 1
    perg3 = input("10 + 10 é 20? ")
    if(perg3 == "sim"):
        print("Parabens acertou")
        ponto3 += 1
    else:
        print("Poxa, iremos melhorar")

    soma = ponto1 + ponto2 + ponto3

    print(f"Sua pontuação foi de: {soma} ")
    if (soma >= 2):
        print("Parabens voce ganhou!")
    else: 
        print("você perdeu! ")
    joga = input("Deseja jogar novamente? ")