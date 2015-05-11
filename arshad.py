#!/usr/bin/env python
# -*- coding: utf-8 -*-
##### VARIABLES
chiffre=1
fin =50
a=0
x=0
i=0
r=0
li=[]
li2=[]
loop=True
g =0
li3=""
##### DEFINITION
def diviseur(chiffre):
#      print("Le diviseur est :")
      chiffre=str(chiffre)
      x=0
      for i in range (len(chiffre)):
            x=x+int(chiffre[i])
#      print(x)
      return(x)

def arsh(x):
      x= diviseur(chiffre)
      r=int(chiffre)%x
      if (r==0):
#            print("le chiffre ",chiffre," est un nombre arshad")
            li.append(chiffre)
            
      else:
            li2.append(chiffre)
            
##### DEBUT DU PROCESS
while (loop==True):
      chiffre =int(input("Entrez le début du process "))
      fin =int(input("Entrez la fin du process "))
      print("\nVoici les chiffre d'harshad départ de ",chiffre," à ",fin,":")
      while (chiffre<(fin+1)) :
            diviseur(chiffre)
            arsh(x)
            chiffre+=1
      print("\nLes chiffres sont harshad :\n",li)
      if (li2==[]):
            print("\nIl n'y a pas de nombres non harshad")
      else:
            print("\nLes chiffres non harshad sont :\n",li2)
      print("\n////// Fin du travail ////")
           
      loope=int(input("Voulez vous continuer ? (1=Oui 0=non) "))
      if (loope==1):
            loop=True
            print("\n\n")
      else:
            loop=False
            print("\n Fin du programme")


