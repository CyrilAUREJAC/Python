#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-

#Date : 27/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice

import os
os.chdir("C:/Users/SkoreGaming/Documents/GitHub/Python")

fichier=open("exo6.py", "r")

print(fichier)
print(fichier.read())


fichier.close()

#autre méthode d'ouverture, pas besoin de fremeture, il va le fermer lors de l'arrete du programme
with open("exo6.py", "r") as fichier:
	print(fichier.read())


#on affiche la taille du fichier. On a pas besoin de l'ouvrir ou de le fermer
print(os.path.getsize("C:/Users/SkoreGaming/Documents/GitHub/Python/exo6.py")) #taille en octet
print(os.stat("C:/Users/SkoreGaming/Documents/GitHub/Python/exo6.py").st_size) #idem


print(fichier.closed) #on verifie que le fichier est fermé =True

