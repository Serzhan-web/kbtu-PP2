#8
def spy_game(N):
    check = []
    for i in N:
        if i in [0,7]:
            check.append(i)
    if check == [0,0,7]:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #False
print(spy_game([1,7,2,0,4,5,0])) #False
