#                Lendo o número inteiro
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

#                 Definindo Linha
def linha(tam=42):
    return '-' * tam

#                  Definindo cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#                  Configurando as opçoes de Menu
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1 
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
    

