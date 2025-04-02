# Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro valído.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro valído.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados de dados interrompida pelo usuário.')
            return 0
        else:
            return n

n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')

print(f'O valor digitador foi {n1} e o Real foi {n2}')