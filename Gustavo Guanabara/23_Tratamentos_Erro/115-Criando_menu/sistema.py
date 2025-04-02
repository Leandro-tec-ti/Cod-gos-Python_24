from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'estudo.txt'

if not arquivoExixte(arq):
    criarAquivo(arq)
    

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de lista o conteúdo de um arquivo!
        lerAquivo(arq)
    elif resposta == 2:
        # Opção de cadastraaar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(2)