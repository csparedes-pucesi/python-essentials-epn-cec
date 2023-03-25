# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:02:40 2019
@author: CEC
"""
#lista1=["R1","R2","R2","R3"]
#for i in range(0,len(lista1)):
#    print(i)
# 0
# 1
# 2

cadena = 'I don\'t know how to spell IoT ! Is it IoT or iot ? What does iot mean anyway?'
#print(type(cadena))
#print(cadena)

lista = cadena.split(" ")
#print(type(lista))
#print(lista)

contador=0
for a in lista:
    if "IoT" in a:
        contador=contador+1
    elif "iot" in a:
        contador= contador+1
print(contador)

#for i in range(0,len(lista)):
#    print(i)