#Booleans represent one of two values: True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(42 == 2077) #Output: False
print("Ali" != 'makpal') #Output: True
print(8080 > 6800) #Output: True

#Print a message based on whether the condition is True or False:
a, b = 42, 2077
if b > a: #True
  print("b is greater than a") #Python output this sentence
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return
#Evaluate a string and a number:
print(bool(""), bool("Intel")) #Output: False True
print(bool(0), bool(2077)) #Output: False True
"""
Most Values are True:
Almost any value is evaluated to True if it has some sort of content.
1) Any string is True, except empty strings.
2) Any number is True, except 0.
3) Any list, tuple, set, and dictionary are True, except empty ones.

Some Values are False
1) In fact, there are not many values that evaluate to False, except empty values,
such as (), [], {}, "", the number 0, and the value None. 
2) And of course the value False evaluates to False.
"""
#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False,
and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #Output: False

#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction()) #Output: True

"""
Python also has many built-in functions that return a boolean value,
like the isinstance() function, which
can be used to determine if an object is of a certain data type:
"""
x = 2077
print(isinstance(x, int)) #Output: True
