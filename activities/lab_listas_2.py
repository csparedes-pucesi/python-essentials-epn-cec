# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:42:22 2023

@author: CSPAREDES

Su tarea es escribir y probar una función que toma dos argumentos (un año y 
un mes) y devuelve el número de días para el par mes / año dado (aunque solo 
febrero es sensible al valor del año, su función debería ser universal).

La parte inicial de la función está lista. Ahora, modifique a la función para 
que use la opción de return  None si sus argumentos no tienen sentido.

Por supuesto, puede (y debe) usar la función previamente escrita y probada 
(LAB Listas y return). Puede ser de mucha ayuda. Lo alentamos a que use una 
lista con los meses. Puede crearlo dentro de la función: este truco acortará 
significativamente el código.
"""


def isYearLeap(year):
    if(year%4==0):
        return True
    else:
        return False


def daysInMonth(year, month):
    monthsList = [31,28,31,30,31,30,31,31,30,31,30,31]
    isYearLeapVar = isYearLeap(year)
    if isYearLeapVar == True:
        monthsList[1] = monthsList[1] + 1
    days = 0
    for x in range(month):
        days += monthsList[x]
    return days


testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

    yr = testYears[i]

    mo = testMonths[i]

    print(yr, mo, "->", end="")

    result = daysInMonth(yr, mo)
    
    print(result, ":", end= ' ')

    if result == testResults[i]:

        print("OK")

    else:

        print("Failed")

