#11
def is_palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

print(is_palindrome("Я с леди все же свиделся")) #True
print(is_palindrome("Коту скоро сорок суток")) #True
print(is_palindrome("hello")) #False
print(is_palindrome("А роза упала на лапу Азора")) #True
