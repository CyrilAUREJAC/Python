#!/usr/bin/env python3

# -*- coding: utf-8 -*-

#Date : 26/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice Recherche numero 2

from random import randint


jeu=True


while jeu:

	#initialisation d'une liste de 10 élements de 1 à 10
	tab_jeu=[]
	for i in range(0,10):
		tab_jeu.append(randint(1,10))

	#On trie le tableau
	tab_jeu.sort()

	#initialisation de la valeur recherchée
	num_cherche=0
	while num_cherche<=0 or num_cherche>10:
		num_cherche=input("Quel numéro allant de 1 à 10 souhaitez vous chercher ? ")
		# On convertit
		try:
		 num_cherche = int(num_cherche)
		except ValueError:
		 print("Ce n'est pas un entier ! ")
		 num_cherche=0
		 continue
		if num_cherche > 10 or num_cherche<=0 :
  		 print("La valeur saisie n'est pas comprise entre 1 et 10.")

	#On compare les valeurs du tableau 1 à 1 avec la valeur recherchée
	for i in tab_jeu :
		if num_cherche==i:
			win=True
		elif num_cherche<i:
			break
		else:
			win=False

	#affiche le tableau et on indique sa position dans l'ordre de tirage (comme si c'etait un loto)
	for i, elt in enumerate(tab_jeu):
		print("Le chiffre tiré en {} est le {}".format(i,elt))

	#Si le numéro recherché s'y trouve, c'est gagné
	if win:
		print ("Gagné !")

	else:
		print("Perdu")

	del tab_jeu

	#On quitte ?
	rep=input("Souhaitez vous quitter ? ")
	rep=rep.lower()
	if(rep=="q"):
		jeu=False
	else:
		jeu=True







