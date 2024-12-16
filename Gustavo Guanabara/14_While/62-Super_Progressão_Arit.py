## Refaça p desafio 061, lendo o primeiro termo e a razão de uma PA, 
# Perguntando ao Usuário se ele quer mostrar mais Alguns termos. programa deve encerrar quando ele Digitar "0"


print('Gerador de PA')
print('-='* 10)
primeiro = int(input("primeiro termo: "))
razao = int(input("Razãp da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while cont <= total:
        termo += razao
        print(f'{termo} --->>>')
        cont += 1
    print("Pausa")
    mais = int(input("quantos termos você quer mostrar a mais? "))
print("Fim")