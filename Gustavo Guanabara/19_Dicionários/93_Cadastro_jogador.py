# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: ==> '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? ==> '))
for c in range(0,total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ==> ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'* 30)
print(jogador)
print('=-'* 30)

for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('=-'* 30)
print(f'O jogador {jogador["nome"]} jogou {total} partidas e marcou {jogador["total"]} gols. ')