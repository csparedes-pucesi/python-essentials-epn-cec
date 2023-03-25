# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:08:44 2023

@author: CSPAREDES

Su tarea es escribir y probar una función que toma un argumento (un año) y
devuelve Verdadero si el año es bisiesto o Falso de lo contrario.

La semilla de la función está en el código adjunto.

Nota: también hemos preparado un breve código de prueba, 
que puede usar para probar su función.

El código usa dos listas: una con los datos de prueba y la otra con los 
resultados esperados. El código le dirá si alguno de sus resultados no es válido.
"""

def isYearLeap(year):
    if(year%4==0):
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

    yr = testData[i]
    
    print(yr,"->",end=" ")
    
    result = isYearLeap(yr)
    
    if result == testResults[i]:

        print("OK")

    else:
        print("Failed")
        
