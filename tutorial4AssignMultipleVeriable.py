# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:16:43 2024

@author: h4tec
"""
print("*****simple unpack collection*****")

x, y,z  =  "Orange", "banana", "cherry"


print(x ,y ,z )

x = y = z  =  "Orange"
print("********simple unpack collection one value to multiple********")
print(x ,y ,z )

fruits = ["Orange", "banana", "cherry"]
x, y, z =fruits
print("********smany vlues to multiple variables********")
print(x ,y ,z )
print (fruits[0])

print("*****for loop for collection****")
count = 0
for i in fruits:
    print(fruits[count])
    count+=1