

def aumentar(preco = 0, taxa = 0, formato=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formato is False else moeda(resposta) # <----------- if formato is False else moeda(resposta)
                                                             #                         |
                                                             #                         |
def diminuir(preco = 0, taxa = 0, formato=False):            #                         |
    resposta = preco - (preco * taxa/100)                    #                         |
    return resposta if formato is False else moeda(resposta) # <-----------------------|
                                                            #                          |
def dobro(preco = 0, formato=False):                        #                           ---->>> é mesma coisa 
    resposta = preco * 2                                    #                          |
    return resposta if not formato else moeda(resposta)     # <------------------------|
                                                            #                          |
def metade(preco = 0, formato=False):                       #                          |
    resposta = preco / 2                                    #                          |
    return resposta if not formato else moeda(resposta)     # <----------- if not formato else moeda(resposta)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') # .replace() --->>> substitui os caracteres 

def resumo(preco=0, taxaa=10, taxar=5):
    print('=-' * 30)
    print('RESUMO DO VALOR'.center(30)) # <<--- .center() é para o cabeçalho ficar centralizado. 
    print('=-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}') # <<<---    (\t) = Centreliza no terminal a resposta para ficar em ordem
    print(f'Dobro do preço: \t{dobro(preco, True)}')#              nome se dá de tabulação
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('_-' * 30)

    return