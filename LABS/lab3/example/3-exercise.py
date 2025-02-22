def get_max(x,y,z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    else:
        return z
    
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
k=get_max(a,b,c)
print(k)