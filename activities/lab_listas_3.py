# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:58:36 2023

@author: CSPAREDES

Su tarea es escribir y probar una función que toma tres argumentos (un año, 
un mes y un día del mes) y devuelve los días correspondiente del año, o 
devuelve None si alguno de los argumentos es inválido.

Use las funciones previamente escritas y probadas. 
Agregue algunos casos de prueba al código. 
"""


def isYearLeap(year):
    if(year % 4 == 0):
        return True
    else:
        return False


def daysInMonth(year, month):
    monthsList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    isYearLeapVar = isYearLeap(year)
    if isYearLeapVar == True:
        monthsList[1] = monthsList[1] + 1
    days = 0
    for x in range(month):
        days += monthsList[x]
    return days


def dayOfYear(year, month, day):
    try:
        daysCounted = 0
        for x in range(year):
            if(x < year):
                if(isYearLeap(x)):
                    daysCounted = daysCounted + 366
                else:
                    daysCounted = daysCounted + 365
            else:
                daysCounted = daysCounted + daysInMonth(x, month) + day
        return daysCounted        
    except:
        return None


print(dayOfYear(2000, 12, 31))