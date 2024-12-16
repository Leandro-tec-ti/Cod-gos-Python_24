# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Que ano deseja analisar? ')) 
if ano == 0: 
    ano = date.today().year# <<<---biclioteca para busca a data atual, só o ano "today().year"  
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#<<--Calculo para descobrir se o ano é BISSEXTO ou nao.
    print(f'O ano {ano} é BISSEXTO')
else:
    print('O ano {ano} nãoi é BISSEXTO')