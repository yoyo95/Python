#Savoir si c'est un triangle parafait il faut que les
# 3 cote soit impair
from math import *

cotea =0
coteb =0
cotec =0

print('bienvenue sur le programme traiangle parfais\nIl faut connaitre deux cotés au minimum')
hypo = int(input('Connaissez-vous l\'hypotenuse ? (0=Non 1=Oui)'))
if (hypo==1):
      cotea = int(input('Entrez le premier coté '))
      cotec = int(input('Entrez l\'hypothenuse '))
      cotea = cotea * cotea
      cotec = cotec * cotec
      coteb = cotea+cotec
      coteb= sqrt(coteb)
      coteb = int(coteb)
      cotebc = coteb%2
      if (cotebc==0):
            print('C\'est un triangle parfais les valeur sont :',sqrt(cotea),coteb,sqrt(cotec))
      else :
            print('Ce n\'est pas un triangle parfais')
elif (hypo==0):
           cotea = int(input('Entrez le premier coté '))
           cotec = int(input('Entrez le second coté '))
           cotea = cotea * cotea
           cotec = cotec * cotec
           coteb = cotea+cotec
           coteb= sqrt(coteb)
           coteb = int(coteb)
           cotebc = coteb%2
           if (cotebc==0):
                 print('C\'est un triangle parfais les valeur sont :',sqrt(cotea),sqrt(cotec),coteb)
           else :
                 print('Ce n\'est pas un triangle parfais')
else :
      print('vous ne savez pas c\'est quoi')
