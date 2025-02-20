def d34(n):
    result=[]
    for i in range(n,0,-1):
        result.append(i)
    return result

n=int(input("n:"))
k=d34(n)
print(k)