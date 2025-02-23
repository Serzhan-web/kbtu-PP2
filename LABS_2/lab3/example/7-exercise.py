def fibanachi(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibanachi(n-1)+fibanachi(n-2)
    
k=int(input("san:"))
print(fibanachi(k)) 