import os
import string

with open("sometext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()