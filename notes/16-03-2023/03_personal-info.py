# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:30:00 2023

@author: CSPAREDES

Script to Collect Personal info
"""

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
location = input("Where do you live? ")
age = int(input("How old are you? (Only int) "))
# space = " "
# print("For{}those{}who{}lived{}in{}a{}secret{}land{}of{}{}".format(
#     space, space, space, space, space, space, space, space, space, location))
# print("Most{}known{}to:{}{}{}{}{}{}who{}keeps{}{}{}years{}old{}".format(space, space,
#       space, first_name, space, last_name, space, space, space, space, age, space, space, space))


print("Nombres completos: {} {}".format(first_name, last_name))
print("Ciudad Natal: {}".format(location))
# 6-11 infante
# 12-17 adolescente
# 18-65 adulto
# 65-100 tercera edad
if age >= 6 and age <=11:
    print("Eres un infante feliz")
elif age >= 12 and age <= 17:
    print("Eres un adolescente irritable")
elif age >=18 and age <= 65:
    print("Eres une adulte amargade")
elif age >= 65:
    print("Eres une abuele calmade")
else:
    print("Ingrese bien la información por favor")
    
    
    
    
