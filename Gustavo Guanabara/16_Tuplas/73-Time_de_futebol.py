# Crie uma TUPLA preenchida com os 20 primeiros colocados da tabela do Brasileirão na ordem de colocação. depois mostre:
# A- Os 5 Primeiro colocados. 
# B- Os últimos 4 colocados
# C- Times em Ordem Alfabética.
# D- Em que posição está o time do Flamengo

times = ('Flamengo','Atlético-MG','Palmeiras','Grêmio',
'Botafogo','Red Bull Bragantino', 'Fluminense','Athletico-PR',
'Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians',
'Cruzeiro','Vasco','Bahia','Vitória','Juventude','Criciúma','Atlético-GO')

print('-=' * 30)
print(f'Lista de times: \n{times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 30)
print(f'Times em Ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'Flamengo está na {times.index("Flamengo")+1}ª posição.')
print('-=' * 30)