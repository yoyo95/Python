Valeur= int(input("Entres la valeur que tu veux convertir (en EUR) "))
print ("maintenant tu vas choisir la devise :")
Devise= int(input(" 1) Dollar \n 2) Shekel \nQue choisis tu ? "))
if Devise == 1:
    dollar = Valeur * 1.28077
    print (Valeur,"€ = ",dollar,"$")
          
if Devise == 2:
    chekel = Valeur * 4.77921
    print (Valeur,"€ = ",chekel,"ILS")
else:
    print("erreur de saisit")
