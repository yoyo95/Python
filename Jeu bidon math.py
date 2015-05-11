##JEU BIDON DE MATH
from random import *

print('Bienvenue sur un jeu simple \n vous devez completez le')
r = int(input('Voulez vous jouer ? (0=non 1=oui) '))
if (r==1):
      replay =True
else :
      replay =False

p=0
g=0
while (replay ==True):
      a= random()
      a= a*10
      d=0
      a=int(a)+1
      while (a<100):
            print('On veut arriver a 100 il faut rajouter combien a :',a)
            c = int(input('\n'))
            if (c>99):
                  p+=10
            else :
                  a =a +c
                  d+=1
            if (d>3):
                  p+=1
                  print('')
            else :
                  g+=1
                  #('Vous avez gagné en ',d,'fois')
            r = int(input('Voulez vous rejouer (0=non 1=oui)'))
            if (r==1):
                  replay= True
            else :
                  replay= False
print('Fin du jeu')
if (p !=0 or g !=0):
      print('gangné :',g,'\nperdu :',p)
