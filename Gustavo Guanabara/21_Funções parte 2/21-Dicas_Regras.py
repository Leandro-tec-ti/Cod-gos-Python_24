
#                                       INTERACTIVE HELP              <<<--- tradução: ajuda interativa
# Comando é : "help()"
# Exemplo de solicitar a ajuda interativa é : 
# help(print) <<--- aqui o terminal vai te trazer qual é a função do print dentro do python
# help(input)       <<--- aqui o terminal vai te trazer qual é a função do input dentro do python e assim por diante.


#                                      DOCSTRINGS 
# Para Utilizar uma DOCSTRINGS é necessário utilizar 3x aspas duplas assim --->> """ """

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
           função criada por Leandro Fernandes
    """
    c = i #                           |
    while c <= f:#                    |
        print(f'{c} ', end='')#       |_______ --->>> Tudo que estiver dentro = """ """ vai servir como manual de 
        c += p #                                       instruçoes do conteúdo inserido, dentro da = def contador(i, f, p)
    print('FIM')

help(contador)#   <<<---- Aqui com "help(contador)" vai me trazer o manual de dentro def no terminal na hora que executar
print('-=' * 30)

#                                      PARÂMETROS OPCIONAIS
# Para utilizar um PARÂMETRO OPCIONAL é só colocar "=0" depois do (a, b ou c) ficando assim:  def somar(a=0, b=0, c=0):
# Essa função vai ajudar para quando receber menos parametros dentro do "somar()"
def somar(a=0, b=0, c=0):
    """
    -> Faz uma contagem e mostra na tela.
    :param A: inicio da contagem
    :param B: fim da contagem
    :param C: passo da contagem
    :return: sem retorno
           função criada por Leandro Fernandes
    """
    s = a + b + c
    print(f'A soma é: {s}')
somar(3, 2)
print('-=' * 30)


#                                       ESCOPO DE VARIÁVEIS 

def teste(b):#       |---->>> ATENCÃO: "global a" estou dizendo para o programa não criar uma nova variável "a" e sim substiua o valor dela 
    global a # <<<---|      ex: "a" de fora da definição tem um valor de 5, ele deixa de valer 5 para valer 8
             #               Assim "a" tem um valor de 8 de forma global 
    a = 8 #<<---"a = 8" foi declarado 8 dentro "def" e só irá funcionar dentro da definição que é chamado de (escopo local) ou variável local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
# programa principal
a = 5 #<<---"a = 5" foi declarado 5 fora "def" e irá funcionar de forma Global, dentr e fora da definição, que é chamado de (escopo Global) ou variável Global
teste(a)
print(f'A fora vale {a}')
print('-=' * 30)


#                                      RETORNO DE VALORES 
def somar1(a=0, b=0, c=0):
    s = a + b + c
    return s # <<--- "return" essa função vai dá um retorno com calculo feito pra "s" 

# Programa principal
r1 = somar1(3, 2, 5) # foi criando uma variável para receber a resposta de "s" 
r2 = somar1(4, 5, 1)
n1 = int(input('Digite 1º número: => '))
n2 = int(input('Digite 2º número: => '))
n3 = int(input('Digite 3º número: => '))
r3 = somar1(n1, n2, n3)
print(f'A resposta do primeiro calculo foi {r1}\n A resposta do segundo calculo foi {r2}\n A resposta do terceiro calculo foi {r3} ')
print('-=' * 30)


#                                     CALCULANDO UM FACTORIAL
def fatorial(num=1):
    f = 1 # -----------------------|
    for c in range(num, 0, -1):#   | <<<--- Calculo para achar o fatorial
        f *= c #                   |
    return f # --------------------|
    

n = int(input(f'Digite um número para o factorial: => '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')