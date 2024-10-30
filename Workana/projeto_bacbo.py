import 
#O programador precisa ter conhecimento em webscrap e socket.


#Quero que o bot reconheça as cores na vertical de acordo com o histórico do jogo.
#Quero configura-lo para ele entrar apartir da segunda cor como no modelo abaixo.

#🔵🔴🔵
#🔴🔵🔴
#🔵🔴🔵
#O bot reconhecerá as oportunidades de apostas após a segunda cor na vertical encontrada no histórico.
#Obs: será cadastrada no bot outras regras como essa acima.

matriz = [
    ['  ','🔴','🔵'],
    ['🔴','🔵','🔴'],
    ['🔵','🔴','🔵']
    ]
linha = input("Qual a cor desejada, Vermelha / Azul? \n")
