# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem 
# com tamanho adaptável.                                  Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~                                                    Olá, Mundo!                                       ~~~~~~~~~ 

def escreva(msg):
    #                    |---------- <<<--- "+ 4" é para centralizar o texto junto com o "print(f'  {msg}')" dando espaço.
    #                    |
    tamanho = len(msg) + 4 # <<<--- o "len()" vai me dá a quantidade de caracteres usadas na msg (tamanho do texto)
    print('~' * tamanho)# ----
    print(f'  {msg}')          #     | <<--- Aqui estou pedido para quantidade do caracteres ser do tamanho da msg
    print('~' * tamanho)# ----

#    Programa Principal
escreva(" Leandro Fernandes ")
escreva(" Eu sou casado ")