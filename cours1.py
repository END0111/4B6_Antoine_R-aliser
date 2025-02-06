import time
# Variables
compteur = 0  # int
a = "allo"  # string
b = "bonjour"  # string
timer = True  # boolean

while timer:
    if compteur == 0:
        print(a)
        compteur += 1 # mettre le compteur à 1 donc allo est faux et bonjour est vrai
    else:
        print(b)
        compteur -= 1 # Remettre le compteur à 0
    time.sleep(1)  # Attendre 1 seconde

#this is a very useful comment that will be ignored by the interpreter