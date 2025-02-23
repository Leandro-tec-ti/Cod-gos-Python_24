
teste = [] #                <<<--- Lista    

                      # adicionando o primeiro dado da lista
teste.append('Leandro') # <<<--- Estou adicionando dados nesse caso "Leandro" na lista
teste.append('36')
galera = []            # Criando uma Segunda lista para sobrepor a lista "teste"
galera.append(teste[:])  # Aqui estou criando uma copia da Lista "teste" com a função "[:]" 
#  adciondando mais um dado atraves da lista "galera" com isso o resultado vai ser a informação da lista "teste" = 
# ['Leandro', 36], mais a informação adcionada da lista "galera"

#                             adicionando o segundo dado da lista
teste[0] = 'Jessica'
teste[1] = "34"
galera.append(teste[:])# Aqui estou criando uma copia da Lista "teste" com a função "[:]" 
#  adciondando mais um dado atraves da lista "galera" com isso o resultado vai ser a informação da lista "teste" = 
# ['Leandro', 36], ['Jessica', '34'] mais a informação adcionada da lista "galera"

#                             adicionando o terceiro dado da lista
teste[0] = 'Dandara'
teste[1] = '9'
galera.append(teste[:])# Aqui estou criando uma copia da Lista "teste" com a função "[:]" 
#  adciondando mais um dado atraves da lista "galera" com isso o resultado vai ser a informação da lista "teste" = 
# ['Leandro', 36], ['Jessica', '34'], ['Dandara', '9'] mais a informação adcionada da lista "galera"

#                             adicionando o quarto dado da lista
teste[0] = 'Marcia'
teste[1] = '52'
galera.append(teste[:])# Aqui estou criando uma copia da Lista "teste" com a função "[:]" 
#  adciondando mais um dado atraves da lista "galera" com isso o resultado vai ser a informação da lista "teste" = 
# ['Leandro', 36], ['Jessica', '34'], ['Dandara', '9'], ['Marcia', '52'] mais a informação adcionada da lista "galera"

print(galera) #<<<--- Desta forma estou pedido para imprimir todos os dados da lista "galera"
print(galera[0]) #<<--- se eu adcionar "[0]" estou pedindo para imprimir só o dado da casa 0 dentro da lista "galera"
print(galera[3][0])#<--  "[3][0]" estou pedindo para me dá só o item 0 que está dentro da casa 3    
# EXEMPLO:
# __________________  ___________________  __________________  ____________________
#|  ['Leandro', 36],|| ['Jessica', '34'],|| ['Dandara', '9'],||['Marcia', '52'] <--+-- = Lista "teste"
#|  [   0        1] || [   0          1] || [   0        1 ] ||[   0        1 ]    |
#|__________________||___________________||__________________||____________________|<--- = Lista "galera"
#          0                  1                 2                       3
print('-=' * 30)
#para cada teste em galera
for t in galera:
    print(t[0]) #<<<--- Aqui estou pedindo para me dá o item 0 de cada lista "teste" que está dentro da lista "galera"
    #  neste casa que são os NOMES das Pessoas.
    print(f'{t[0]} tem {t[1]} anos de idade.') # <<< --- Também pode ser assim.
print('-=' * 30)

turma = []
dado = []
#para c repetir 3x (ranger é repetição)
for c in range(0, 3):
    dado.append(str(input("Digite seu nome: "))) #<<-- Aqui estou buscando a informação nome para colocar na lista "dado"
    dado.append(int(input("digite sua idade: ")))#<<-- Aqui estou buscando a informação idade para colocar na lista "dado"
    turma.append(dado[:])# Aqui estou Criando uma cópia da Lista "dado" e colocando cópia dentro da lista "turma"
    dado.clear()# <<--- aqui estou pedindo para Excluir na sequência.
print(turma)

maior = menor = 0 
#para cada dado em turma
for d in turma:
    if d[1] >= 21:
        print(f'{d[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{d[0]} é menor de idade. ')
        menor += 1
print(f'{maior} pessoas é maior de idade e {menor} pessoas é menor de idade. ')