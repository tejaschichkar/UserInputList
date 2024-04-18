# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:53:29 2024

@author: tejas
"""

list1 = []

x = False

while(x == False):
    item = input("Enter item to add in list \n")
    list1.append(item)
    print(list1)
    y = input("type y if you want to add more item or n if you are done \n")
    if y == 'n':
        x = True
        print('Here is your final list :', list1)
    else:
        x = False