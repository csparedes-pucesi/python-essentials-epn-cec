# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:21:22 2023

@author: csparedes
"""

file=open("devices.txt", mode="a")
while True:
    newItem=input("Ingrese el nuevo dispositivo: ")
    if newItem=="exit":
        print("All done!")
        break
    file.write(newItem + " ")
file.close()