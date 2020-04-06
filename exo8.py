#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-

#Date : 27/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Exercice

import datetime
import time

print(datetime.datetime.now())

x=datetime.datetime.now()

print (x.year)
print (x.month)
print(x.day)
print(x.isocalendar()[1]) #numero de la semaine
print(x.isocalendar()[2]) #numero du jour