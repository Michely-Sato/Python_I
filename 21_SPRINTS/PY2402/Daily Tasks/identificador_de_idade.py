# -*- coding: utf-8 -*-
"""identificador de idade

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T30xjoSYyLZ36q1VIM6e_NtVeKub3kt4
"""

d=float(input("Digite sua data de nascimento: "))

a=float(input("Digite o ano atual: "))

i=a-d

if i>17.9:
  print("Você é maior de idade com ",i," anos")
else:
  print("Você é menor de idade com ",i," anos")