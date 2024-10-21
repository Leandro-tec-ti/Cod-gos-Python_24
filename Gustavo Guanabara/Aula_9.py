
Frase = "Curso em video Python" 
# O python irá guarda na memoria do pc e atribuir cada letra dessa frase (inlcuíndo os espaços) vai receber um indice, 
#ou seja um numero para cada letra da Frase:
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20

#                                 Fatiamento
Frase[9] # <<<--- Essa formula irá me trazer a infomação que ira esta no numero 9, que no caso é a letra: V
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                         ^
Frase[9:13] #<<<---Essa formula irá te dá a informção do numero 9 até o 12 e não até o 13 "ultimo numero é desconsiderado"
#(obs: só até o 12 pq o Python sempre entende até o um numero abaixo, pq ele considera o "0" como um numero na contagem).
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                         ^------------^
Frase[9:21] #<<<--- Essa formula vai te dar a informção do 9 até o final (pq não a frase só vai ate o numero 20).
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                         ^------------------------------------------------
Frase[9:21:2]#<<<--- Essa formula irá te dá a informação, mas sempre pulando uma casinha.
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                         ^ --x-- ^ ---x-- ^ ---x--- ^ --x-- ^ --x-- ^ --x-
Frase[:5]#<<<---Essa formula irá te dá a informação do inicio até o 4, (antes do ":" esta vazio, segnifica que é o inicio)
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
# --------------- ^
Frase[15:]#<<<--- Essa formula irá te dá a informação do numero 15 até o final.
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                                                    ^ -------------------
Frase[9::3]#<<<--- Essa formula ira te dá a informação do 9 até po final, mas pulando 2 casas,
#(entre os "::"está vazio indicando ir até o final e depois tem o numero "3" indicando para contar de 3 em 3 casas)
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                         ^---x----x-- ^---x----x--- ^---x---x-- ^---x---x--

#                                       Análise
len(Frase)#<<<--- função len é o comprimento da quantidade de caracteres "casas" itilizada na variação (Frase)
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
# ^----------- len vai te dá a quantidade de casas que esta sendo utilizada -------------^ = neste caso são 21 caracteres
Frase.count('o')#<<<--- Essa formula vai contar a quantidade de letra que tem dentro da Frase, 
#neste caso o (.count) esta pedido para contar quantas letras "o" tem nas casinhas 
#(obs: letra maiuscula é difereente da minusculo)
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                 *                                       *                         *      = neste caso são 3 letras
Frase.count('o',0,13)#<<<---Essa formula vai considerar do "0" ao "12" a quantidade "o" dentro das casinhas
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
# ^-------------- * ----------------------------------^                                    = neste caso 1 letra
Frase.find("deo")#<<<---essa Formula irá te dá onde foi o lugar que começou o "deo" 
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                                  ^                                      = neste caso comerçou no 11
Frase.find("Android")#<<<--- se você solitar uma informação que nao tem nas casinhas, 
#irá receber a informação "-1" isso indica que ela não exite.
"Curso" in Frase #<<<--- essa formula "in" irá dizer se existe a palavra curso nas casinhas, 
#caso tenha irá aparecer a palavra True (verdadeiro)

#                                      Transformação
Frase.replace("Python","Android")#<<<--- Essa formula vc consegue trocar as mensagem entre "".
#Neste caso iria retirar a msg Python e iria substituir pela palavra Android.
#[C] [u] [r] [s] [o]  [ ]  [e] [m]  [ ]  [V] [i] [d] [e] [o]  [ ]  [A] [n] [d] [r] [o] [i] [d]  <-- substituição
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20  21
Frase.upper()#<<<--- um metodo para torna toda mensagem em letra maiuscula

Frase.lower()#<<<--- um metedo para tonar toda mensagem em letra minuscula

Frase.capitalize()#<<<--- um metodo para deixar apenas a primeira letra da mensagem maiuscula

Frase.title()#<<<--- um metodo para deixar a letra maiuscula de cada palavra da mensagem.
#(como ele identificar cada palavra, atravé dos espaços de cada palavra)

Frase.strip()#<<<--- Essa formula elimina os espaços vazios somente no inicio e no final da mensagem. ex:
#[ ] [ ] [ ] [A] [p]  [r]  [e] [n]  [d]  [a] [ ] [P] [y] [t]  [h]  [o] [n] [ ] [ ] [ ] [ ]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
# ^   ^   ^                                                                  ^  ^   ^   ^ = Esses espaços sinalizado são eliminados
Frase.rstrip()#<<<--- com essa formula o "r" irá retirar somente os espaços vazios do lado direito da mensagem (ultimos espaços da msg)
#[ ] [ ] [ ] [A] [p]  [r]  [e] [n]  [d]  [a] [ ] [P] [y] [t]  [h]  [o] [n] [ ] [ ] [ ] [ ]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                                                                            ^  ^   ^   ^ = Esses espaços sinalizados são eliminados
Frase.lstrip()#<<<--- com essa formula o "l" irá retitar somente os espaços vazios do lado esquerdo da mensagem (primeiros espaços da msg)
#[ ] [ ] [ ] [A] [p]  [r]  [e] [n]  [d]  [a] [ ] [P] [y] [t]  [h]  [o] [n] [ ] [ ] [ ] [ ]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
# ^   ^   ^                                                                              = Esses espaços sinalizados são eliminados

#                                     Divisão
Frase.split()#<<<--- Essa formula o ".split" irá dividir a mensagem por cada palavra em bloco atraves dos espaços entre eles.
#é gerado uma lista com todas as palavras
#[C] [u] [r] [s] [o]      [e] [m]        [V] [i] [d] [e] [o]      [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4        0   1          0   1   2   3   4        0   1   2   3   4   5
#--------0---------       ---1---        ---------2---------      ----------3------------

#                                     junção
"-".join(Frase)#<<<--- o ".join" vai juntar e gerar uma mensagem unica mas com o caracteres "-",
#(se eu deixer espaço entre " " irá aparecer a casinha com espaço)
#[C] [u] [r] [s] [o]  [-]  [e] [m]  [-]  [V] [i] [d] [e] [o]  [-]  [P] [y] [t] [h] [o] [n]
# 0   1   2   3   4    5   6   7     8    9  10   11  12  13   14   15  16  17  18  19  20
#                      *             *                         *                         = sinalizados onde foram adcionados os (-)

# Exercicios do numero 22 ao 27