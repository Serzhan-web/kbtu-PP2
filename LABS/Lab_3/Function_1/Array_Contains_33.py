#7
def has_33(N):
    check = ""
    for i in N:
        check += str(i)

    if '33' in check:
        return True
    else:
        return False

print(has_33([1, 3, 3])) #True
print(has_33([1, 3, 1, 3])) #False
print(has_33([3, 1, 3]), '\n') #False
