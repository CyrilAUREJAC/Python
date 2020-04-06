#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-

#Date : 27/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

dico={}
dic4={}

for cle, valeur in dic1.items():
	dico[cle]=valeur
for cle, valeur in dic2.items():
	dico[cle]=valeur
for cle, valeur in dic3.items():
	dico[cle]=valeur

for d in (dic1, dic2,dic3):
	dic4.update(d)

print(dico)
print(dic4)