
#       EX:
# TUPLAS = ()
# LISTAS = []
# DICIONÁRIO = {}      <<<<---- montagem de um dicionário é atraves de "{}".


#               Dicionários

#           ________________________ <<<--- São as informações que compõem uma lista. ="KEYS" 
#          |                 |
#          |         ________|_______________ <<<--- São as informações que estão dentro do keys, neste caso o valores
#         _|__    __|__    __|__   _|_                que estao inseridos. ="VALUES"
#        |    |  |     |  |     | |   |
dados = {'nome': 'Pedro', 'idade': '25'}
print('=-'* 30)
print(dados['nome']) # <<<--- forma de imprimir os informação do dado que nesse caso é "Pedro"

dados['sexo'] = 'M'  #<<<-- Aqui estou adicionando mais um dado para informação dentro da lista que nesse caso é o "sexo"

del dados ['idade'] #<<<-- Estou removendo um dado de dentro da lista que é "idade" assim  a lista ficara sem as idades
print('=-'* 30)

# Exemplo de estruturação de um dicionário 
print('=-'* 30)
filme = {'titulo': 'star wars',
         'ano': '1977',
         'diretor': 'George Lucas'
    }

print(filme.values()) #<<-- Aqui estou pedindo para imprimir todas as informações que esta dentro dos dados solicitados
print(filme.keys()) # <<-- Aqui estou pedindo para imprimir todos os dados que compõem EX: "nome","idade","sexo" e etc... 
print(filme.items())#<<-- Pedindo para imprimir a lista completa, tanto os dados como as informações inseridas dentro dele.
# para cada keys e valor dentro da lista filme.itens(): <<<--- tradução do for
for k, v in filme.items():
    print(f'{k} é {v}') #<<<--- "{k}" é keys da lista, "{v}" São os valores dentro do keys.

locadora = [] # <<<-- Aqui estou colocando o Dicionário dentro de uma lista
locadora.append(filme)
print(locadora)
print(locadora[0]['ano'])
print('=-'* 30)

print('=-'* 30)
pessoas = {'nome': 'Leandro', 'sexo': 'M', 'idade': 36}
print(pessoas['nome'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos. ') # imprimnindo valores especificos da lista
print(pessoas.keys()) # imprimindo os KEYS da lista
print(pessoas.values())# imprimindo os valores que estão dentro do Keys
print(pessoas.items())# imprimindo a lista completa com todas as informações
for k in  pessoas.keys():
    print(k)   # imprimindo os KEYS da lista
for k in pessoas.values():
    print(k)   # imprimindo os VALUES que estão dentro do keys

for k, v in pessoas.items(): #<<<--- IMPOTANTE: se quiser imprimir o ITEMS preciso colocar duas variantes no for
    print(f'{k} = {v}') #            neste caso foi "k" de keys e o "v" de Values.

pessoas['nome'] = 'Gustavo' # <<<--- Aqui estou Alterando um dado dentro do KEYS "nome" de: Leandro para: Gustavo
print(pessoas)
pessoas['peso'] = 98.5 # <<<--- Aqui estou adicionando mais um KEYS para lista 
print(pessoas)
print('=-'* 30)


#                   Criando um dicionário dentro de uma Lista
print('=-'* 30)
brasil = []  #                             <<<--------        Uma LISTA 
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}# --
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}     #   | <<--- Dicionários
estado3 = {'uf': 'Minas Gerais', 'sigla': 'MG'}  # --

brasil.append(estado1) # --
brasil.append(estado2) #   | <<--- Adcionando os 3 dicionários dentro de uma Lista Brasil
brasil.append(estado3) # --
print(brasil)
print('=-'* 30)


print('=-'* 30)
regiao = {}
brasil_1 = []
for c in range(0,3):
    regiao['uf'] = str(input('Qual é seu estado? ==> '))
    regiao['sigla'] = str(input('Qual é a sigla do seu estado? ==> ')) 
    brasil_1.append(regiao.copy()) # ATENÇÃO IMPORTANTE:  para adicionar listas com dicionarios dentro precisa
#                                    utilizar o elemento ".copy()"
print(brasil_1)
#para cada regiao == r na lista do brasil_1 = Tradução do for
for r in brasil_1:
    # para cada keys e para cada values na lista r.items "items" é igual a lista completa.
    for k, v in r.items():
        print(f'O campo {k} tem valor {v}. ')

print('=-'* 30)