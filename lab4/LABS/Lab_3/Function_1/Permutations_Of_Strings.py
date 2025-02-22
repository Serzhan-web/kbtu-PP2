#5
from itertools import permutations

def print_permutations(s):
    perms = ["".join(p) for p in permutations(s)]
    for p in perms:
        print(p)

word = input()
print_permutations(word)
