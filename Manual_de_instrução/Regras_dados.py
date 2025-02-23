# LISTAS, TULHAS, DICIONARIO, FUNÇOES

TUPLAS = ('0','1','2','3') # Para o programa entender o que é uma tulpa, precisar colocar entre conchetes = ('').
#       TUPLAS SÃO IMUTÁVEIS, NÃO PODEM SER ALTERADAS


                                  # LISTAS

#                            ADICIONANDO E SUBSTITUINDO ELEMENTO NA LISTA
LISTA = ['PAO', 'SUCO', 'PIZZA', 'DOCE']  # Para o programa entender o que é uma lista, precisar colocar entre conchetes = [] .
#       LISTAS SÃO MUTÁVEIS.
print(LISTA)

LISTA[3] = 'PICOLE' # <<-- Esse modelo de código estou fazendo uma sibstituição dentro de um item da lista.
#                          trocando o "DOCE" pelo "PICOLE".
print(LISTA)

LISTA.append('BISCOITO') # <<<--- .append() = é para adicionar mais um item na lista que é o "BISCOITO".
print(LISTA)

LISTA.insert(0,'LATA') # <<<--- .insert() = é para adicionar um item na lista e dizer em que casa será adicionado.
print(LISTA)

#                      APAGAR ELEMENTO NA LISTA
del LISTA[3] # <<-- del ...[] = Aqui estou eliminando um item da lista através do índice ou numero da casa que é a "PIZZA"
print(LISTA)

LISTA.pop(3) #<<--.pop() = Outra maneira de deletar um item da lista que é o "PICOLE"
#                         (por regra esse modo retira o último elemento se deixar ele vazio)
print(LISTA)

LISTA.remove('PAO') #<<-- .remove() = Aqui é remove o valor (precisa colocar o que vc quer remover da lista)
print(LISTA)

#                                  VERIFINCANDO SE TEM O INTEM NA LISTA
if 'PIZZA' in LISTA:
    LISTA.remove('PIZZA') #<<-- Aqui estou colocando uma codição se a "PIZZA" tiver na lista ela vai ser removida.
print(LISTA)

#                                 CRIANDO LISTAS ATRAVÉS DE RANGE
valores = list(range(4,11))# <<<--- list(range()) = Aqui estou declarando uma lista atraves do "range"
print(valores) 

valores = [8,2,5,4,9,3,0] # fora de ordem
print(valores) 

valores.sort() # .sort() = Aqui estou colocando os elementos que estavam fora de ordem em ordem.
print(valores)  

valores.sort(reverse=True) # .sort(reverse=True) = Aqui os valores ficam ordenados de forma inversa ou ao contrário.
print(valores) 

len(valores) # len() = Vai te dá o tamanho da Lista, quantos itens constam na lista.
print(f'{len(valores)}')

