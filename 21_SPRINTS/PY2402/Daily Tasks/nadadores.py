# -*- coding: utf-8 -*-
"""Nadadores.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mztHncMVge1Rqy-_RCtLwsqWwJ_cN-RQ

Classificação de estudantes de um curso de natação em: (Infantil A, Infantil B, Juvenil A, Juvenil B e Adulto)
"""

print('Digite os nomes dos estudantes que deseja adicionar e suas respectivas idades. Quando desejar finalizar o processo de separação digite pressione enter no nome do estudante e 0 na idade')

student=()
age=()
InfantilA=[]
InfantilB=[]
JuvenilA=[]
JuvenilB=[]
Adulto=[]

while student!='':
  student=input('Nome:')
  age=int(input('Idade:'))
  if age >= 18:
    Adulto.insert(1,student)
  elif age >=14:
        JuvenilB.insert(1,student)
  elif age >=12:
      JuvenilA.insert(1,student)
  elif age >=8:
      InfantilB.insert(1,student)
  elif age >=5:
    InfantilA.insert(1,student)
  else:
    print('Muito jovem para adição')

x=()
while x!='':
  x=input('Digite qual classificação deseja verificar')
  if x=='InfantilA':
    print(InfantilA)
  elif x=='InfantilB':
    print(InfantilB)
  elif x=='JuvenilA':
    print(JuvenilA)
  elif x=='JuvenilB':
    print(JuvenilB)
  elif x=='Adulto':
    print(Adulto)



