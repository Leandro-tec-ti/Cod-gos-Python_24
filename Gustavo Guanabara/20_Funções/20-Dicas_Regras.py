#                                  FUNÇÕES

def linha():
    print('<-' * 40)
    

#      Programa Principal
linha()
print('   curso em vídeo   ')
linha()

def titulo(txt):
    print('-' * 40)
    print(txt)
    print('-' * 40)


titulo(" Curso em Vídeo ")
titulo(" Python ")
titulo(" Leandro ")


print()

linha()

# a = 4      ------
# b = 5            |
# s = a + b        |
# print(s)         |
          
# a = 8            |
# b = 9            |--------- Para Subistiur todas somar e forma repetitivas pode fazer com a função "def" exemplo abaixo
# s = a + b        |                |  
# print(s)         |                |

# a = 2            |                |
# b = 1            |                |
# s = a + b        |                |
# print(s)    -----                 |

#                                   |
def soma(a, b):#       <<<----------    pode ser feito desta maneira para simplificar o código
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'Soma A + B = {s}')
#               ----|
#               ____|  <<<--- ATENÇÃO: é necessário ter no mínimo duas linhas de folga para executar a função
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=5)# fiz uma inversão das Variávies trocando o A pelo B. Essa alteração ela pode ser feito desde que vc sinalize

linha()
def contador(*num):  # <<--- "*" é quando vc não sabe a quantidade de número que o usuário vai colocar (desempacotar)
    for valor in num:
        print(f'{valor} ', end='')
    print("  FIM!  ")

    tamanho = len(num) # "len()" é para ver a quantidade de elementos, neste caso são quantos números tem. 
    print(f'Recebi os valores {num} e são ao todo {tamanho} números ')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0              #----
    while pos < len(lst):#    |
        lst[pos] *= 2    #    | <<--- Esse é o cálculo para dobrar os valores dentro da Lista "valores"
        pos += 1         #____|


valores = [6, 3, 9, 1, 0, 2,]
dobra(valores)
print(valores)