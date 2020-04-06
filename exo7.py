#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-

#Date : 27/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice

import random
import os
import pickle

os.chdir("C:/Users/SkoreGaming/Documents/GitHub/Python")

#on crée une liste de 10 entiers random entre 1 et 10
liste=[]
for i in range(0,10):
	liste.append(random.randint(1,10))

#méthode d'ouverture en écriture, pas besoin de fermeture
with open("test.py", "wb") as fichier:
	pick=pickle.Pickler(fichier)
	pick.dump(liste)

#on recupere la liste en lecture
with open("test.py", "rb") as fichier:
	depick=pickle.Unpickler(fichier)
	recup_liste=depick.load()

print(recup_liste)




