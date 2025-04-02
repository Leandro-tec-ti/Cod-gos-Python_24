#                              TRATAMENTOS DE ERRO!!!!
try: # <<<--- É para tentar corrigir exceção ou erro. 

    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

#               -------------->>>  "Exception as erro" = vai sinalizar qual é o erro. 
#       _______|________             Capturar a informação necessária para correção.
#      |                |
except Exception as erro: # <<<--- Se der algum tipo de problema.
    print(f'Infelizmente tivemos um problema :(.  Causa do  problema foi {erro.__class__}') 
                                                                            # |__--->> "{erro.}" estou pedido 
                                                                            #            para qualificar qual foi o erro.
except (ValueError, TypeError):
    print('Tivemos um erro com os dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir este número por zero.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

else: # <<<--- Senão der nenhum problema. (verificar se Try deu certo).
    print(f'O resultado é {r:.1f}')

finally: # <<<--- se colocar é um recado que vai acontecer dando certo ou errado. 
    print('Volte sempre!')
