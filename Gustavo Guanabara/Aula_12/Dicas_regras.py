# Estrutura condicionar aninhadas
nome = str(input('Digite seu nome: ')).lower()
if nome == "gustavo":
    print('Que bonito nome! ')
elif nome == "leandro" or nome == 'jessica' or  nome == 'dandara':
    print("Nossa que legal! ")
elif nome in 'ana beatriz luana marcia': #<<<--- (in) vai simular uma lista com as possibilidades para entrar na elif
    print('Belo nome feminino! ')
else:
    print('Seu nome é diferente! ')
print(f'Tenha um bom dia, {nome}')
