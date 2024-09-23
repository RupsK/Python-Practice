

import os

print("Hello world")

a = "hello"
b = "world"
print(a + '\t' +b)

string = "hello workd \n\n Python Programmin \t"
count = 0
for i in string:
    if(i.isspace()) == True:
        count +=1
print("numbe of spaces in the string", count)