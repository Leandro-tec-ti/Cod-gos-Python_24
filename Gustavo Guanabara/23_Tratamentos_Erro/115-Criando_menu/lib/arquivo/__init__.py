from lib.interface import *

#                       Vendo se Arquivo Existe
def arquivoExixte(nome):
    try:
        a = open(nome, 'rt') # --->>>   "rt" significar  "ler texto"
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
#                       Criando Arquivo
def criarAquivo(nome):
    try:
        a = open(nome, 'wt+') #--->>> "wt+"significa "escrever texto"  o sinal de "+" caso não tenha um texto ele cria um.
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

#                         Lendo Texto dentro do Arquivo
def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f"Erro ao ler o arquivo!  Causa do  problema foi {erro.__class__}")
    else:
        cabeçalho('PESSOAS CADASTRADAS')
       # print(a.read())     --->>> ".read()" Vai mostrar no terminal todas as informaçoes de dentro do arquivo
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # --->> "at" significa append = coolocar coisas dentro do arquivo.
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n') # --->> ".write" é para escrever as informaçoes dentro do arquivo
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f' novo registro de {nome} adcionado.')
            a.close()
