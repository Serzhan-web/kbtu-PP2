#14
# My_Functions.py
def Unique_Elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def Is_Palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

def Histogram(lst):
    for num in lst:
        print('*' * num)

# Main.py
from My_Functions import Unique_Elements, Is_Palindrome, Histogram

print(Unique_Elements([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(Is_Palindrome("А роза упала на лапу Азора"))  # True
Histogram([3, 5, 7])
