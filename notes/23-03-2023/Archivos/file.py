# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:58:59 2023

@author: csparedes
"""
lista=[]
archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    lista.append(item)
    print(lista)
    print(item)
archivo.close()