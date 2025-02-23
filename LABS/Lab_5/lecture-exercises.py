#meta characters
# Quantifieres:
# * ---> 0 или больше
# + --> 1 или больше 
# ?--> 1 или 0 раз появиться
# . --> any symbol
# ^ --> mathching only at the beginning of the string
# $ --> mathching only at the end of the string
# | --> mathcing  two either or,  (roses are red, viloets are blue) --> "roses|violets" 
# [ ] --> множества set of symbols  [abc] [a-z] [a-zA-Z0-9]
# { } --> 

# SPECIAL SEQUENCES
# \d --> any decimal digit
# \D --> any NON-digit character
# \s --> any whitespace character
# \S --> any NON-whitespace chracter
# \w --> any alphanurmer symbol (any digit, symbol or _)
# \W --> any NON-alphanurmer symbol
# \b --> matching pattern only in the beginning of the word
# \B --> matching pattern only in the end of the word


import re

word="AAbbAbbvbAbbBaAbbbbbbbbb qwerty Ab"
print(re.findall("Ab*",word))

print(re.findall("Ab+",word))

print(re.findall("Ab?",word))

print(re.findall("Ab^",word))

print(re.findall("Ab|qwerty",word))

print(re.findall("[ ]",word))

print(re.findall("Ab.",word))

print(re.findall("Ab$",word))

print(re.findall("Ab|qwerty",word))

print(re.findall("{Ab}",word)) 
