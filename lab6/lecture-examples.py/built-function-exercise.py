nums=[1,2,3,4,5,6,7]
print("with list:",list(map(lambda x: x*2,nums))) #list
print("with join:",', '.join(map(str,nums)))   #join 

#reverse 
print(list(reversed(nums)))

soz="qwerty"
print(''.join(reversed(soz)))
 
#filter
import math

num = list(range(1, 51))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

filtered_primes = list(list(is_prime, num))
print(filtered_primes)

#ord() A-65 , chr() 65-A

print(ord('A'))
print(chr(65))

#all() , any()

example=[1,True,"hi",3.14]
example2=[0,True,"hi",3.14]
print("list,all,any:",all(example),any(example))
print("list,all,any:",all(example2),any(example2))