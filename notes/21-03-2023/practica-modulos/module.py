# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:30:22 2023

@author: CSPAREDES
"""

# Module

def test1():
    print("Prueba 1")
    
def fibonacci(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacciRange(n):
    for x in range(n):
        print(fibonacci(x),end=" ")