# -*- coding: utf-8 -*-
"""timextime.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P6fhdrvhPMkK6SCaKW9lzApnhyrytcHC

Código para dizer qual time de uma partida de um jogo ganhou.
"""

time1=int(input('input qtd de gols time1:'))

time2=int(input('input qtd de gols time2:'))

if time1>time2:
  print('vitória do time1!')
elif time1<time2:
  print('vitória do time2!')
else:
  print('empate!')