#Subtopic: Python Variables
"""
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""
x = 52
y = "KBTU - BEST UNIVERSITY"
print(x)
print(y)
#Variables do not need to be declared with any particular type, and can even change type after they have been set.

#Example:
x = 42     # x is of type int
x = "Intel x8086" # x is now of type str
print(x)   #output: "Intel x8086"

#Casting:
x = str(42)    # x will be '42'
y = int(42)    # y will be 42
z = float(42)  # z will be 42.0

"""
GET THE TYPE
You can get the data type of a variable with the type() function.
"""
a = 52
b = "Tyler the creator"
c = 3.1415
print(type(a), type(b), type(c))
#output: <class 'int'> <class 'str'> <class 'float'>

#Single or Double Quotes?
x = "Seriy"
# is the same as
x = 'Seriy'
print(x)

"""
Case-Sensitive
Variable names are case-sensitive.
"""
a = 42
A = 'Fourty two'
#A will not overwrite a


#Subtopic: Variable Names
"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.
"""
myvar = "KBTU"
my_var = "KBTU"
_my_var = "KBTU"
myVar = "KBTU"
MYVAR = "KBTU"
myvar2 = "KBTU"

"""
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Camel Case
myVarExample = 42
#Pascal Case
MyVarExample = 43
#Snake Case
my_var_example = 44


#Subtopic: Assign Multiple Values
#Python allows you to assign values to multiple variables in one line:
x, y, z = "Intel", "Amd", "Motorolla"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = "CPU"
print(x)
print(y)
print(z)

#Unpack a list:
University = ["KBTU", "MUIT", "UIB"]
x, y, z = uinversity
print(x)
print(y)
print(z)


#Subtopic: Output Variables
x = "Python is cool"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "cool"
print(x, y, z)


#You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "bruh"
print(x + y + z) #output: Pythonisbruh

#For numbers, the + character works as a mathematical operator:
x = 42
y = 42
print(x+y) # output : 84

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 42
y = "bruh"
#print(x + y) #mistake

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = "Cool"
y = 42
print(x, y) #output: Cool 42


#Subtopic: Global Variables
#Create a variable outside of a function, and use it inside the function
x = "Za Warudo"
def myfunc():
  print("x equals " + x)
  
myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "awesome" #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x) #output: Python is fantastic
  
myfunc()
print("Python is " + x) #output: Python is awesome

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  
myfunc()
print("Python is " + x)
