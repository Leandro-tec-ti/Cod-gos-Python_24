
# LISTAS

num = [2, 5, 9, 1]
num[2] = 3  #<<<-- dessa forma estou substituindo 9 pelo 3.
num.append(7) #<<-- Aqui estou adcionando o valor 7 na lista com ".append()"
num.sort() #<<<-- o ".sort()" coloca todos em ordem
num.sort(reverse=True) #<<<--- O ".sort(reverse=True)" coloca todos em ordem contrária (sentido contrário)
num.insert(2, 2) #<<--".insert(2, 0)" ele adciona o item na posição exata que desejar (na posição 2 adicionar o 0)
num.pop(2)#<<-- ".pop(2)" ele vai eliminar o numero que tiver na posição 2
if 4 in num:
   num.remove(4)# <<-- ".remove(2)" aqui ele vai remover o numero que esta pedindo dentro da lista ignorando a posição
else:
   print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos. ') #<<<--- "len()" retorna quantos elementos tem. 


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#for cont in range(0, 5):
#   valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores): #<<-- "enumerate()" atribuindo ao "c" antes do "in" acho a posição de cada numero.
   print(f'Na posição {c} encontrei o valor {v}! ')
print('cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]#<<-- IMPORTANTE! sinalização em "[:]" me permite apenas ter uma copia do A para B, ou seja não fazendo uma ligação entre as listas.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')