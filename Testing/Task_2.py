import re

sentence = "Hello World This Is Python"
letter = re.split(" ", sentence)
print(letter)

def all_words_capitalized(letter):
    flag = True
    for i in letter:
        if i[0] < "A" or i[0] > "Z":
            flag = False
    return flag

print(all_words_capitalized(letter))