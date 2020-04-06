#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-

#Date : 27/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice



temperature=input("Votre temperature ? Specifiez C ou F (ex 32F, 56C)")

if temperature[-1:]=="F":
	temperature=int(temperature[:-1])
	convert=round((temperature-(32/9))*5)
	print("= " + str(convert) + " °C ")


if temperature[-1:]=="C":
	temperature=int(temperature[:-1])
	convert=round((temperature/5)+(32/9))
	print("= " + str(convert) + " °F ")
