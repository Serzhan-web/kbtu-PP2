"""
Subtopic: Python Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
"""
CPU = {"Intel":8088, "Motorolla":6800, "AMD":4090}
print(CPU) #Output: {"Intel":8088, "Motorolla":6800, "AMD":4090}
print(CPU["Motorolla"]) #Output: 6800

"""
Ordered or Unordered?
1) When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
2) Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
3) Dictionaries cannot have two items with the same key:
"""
Error_Dict = {
    404:"Error",
    404:"Bad",
    111:"Fallout"
}
print(Error_Dict[404]) #Output: Bad

#To determine how many items a dictionary has, use the len() function:
CPU = {"Intel":8088, "Motorolla":6800, "AMD":4090}
print(len(CPU)) #Output: 3 

#The values in dictionary items can be of any data type:
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
print(Brand_Car) #Output: {'Ford': 1903, 'Ferrari': 1939, 'Bool': False, 'Colors': ['red', 'white', False]}

#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
print(type(Brand_Car)) #Output: <class 'dict'>

#It is also possible to use the dict() constructor to make a dictionary.
cool = dict(name = "Rayan Gosling", age = 42, country = "Canada")
print(cool) #Output: {'name': 'Rayan Gosling', 'age': 42, 'country': 'Canada'}


"""
Subtopic: Access Dictionary Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
print(Brand_Car["Ferrari"]) #Output: 1939
#There is also a method called get() that will give you the same result:
Age = Brand_Car.get("Ford")
print(Age) #Output: 1903
#The keys() method will return a list of all the keys in the dictionary.
Name = Brand_Car.keys()
print(Name) #Output: dict_keys(['Ford', 'Ferrari', 'Bool', 'Colors'])

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Name = Brand_Car.keys()
print(Name) #before the change: dict_keys(['Ford', 'Ferrari', 'Bool', 'Colors'])
Brand_Car["color"] = "white"
print(Name) #after the change: dict_keys(['Ford', 'Ferrari', 'Bool', 'Colors', 'color'])

#The values() method will return a list of all the values in the dictionary.
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Age = Brand_Car.values()
print(Age) #Output: dict_values([1903, 1939, False, ['red', 'white', False]])

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list:
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Age = Brand_Car.values()
print(Age) #Output: dict_values([1903, 1939, False, ['red', 'white', False]])
Brand_Car["Ferrari"] = 2077
print(Age) #After the change: dict_values([1903, 2077, False, ['red', 'white', False]])

#The items() method will return each item in a dictionary, as tuples in a list.
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
MyDict = Brand_Car.items()
print(MyDict) #Output: dict_items([('Ford', 1903), ('Ferrari', 1939), ('Bool', False), ('Colors', ['red', 'white', False])])
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

#To determine if a specified key is present in a dictionary use the in keyword:
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
if "Lamborgini" in Brand_Car:
  print("Yes, 'Lamborgini' is one of the keys in the thisdict dictionary")


"""
Subtopic: Change Dictionary Items
You can change the value of a specific item by referring to its key name:
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Brand_Car["Ford"] = 2018
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs:
Brand_Car.update({"year": 2020})


"""
Subtopic: Add Dictionary Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Brand_Car["Lamborgini"] = 1963
print(Brand_Car) #Output: {'Ford': 1903, 'Ferrari': 1939, 'Bool': False, 'Colors': ['red', 'white', False], 'Lamborgini': 1963}
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added:
Brand_Car.update({"color": "red"})


"""
Subtopic: Remove Dictionary Items
There are several methods to remove items from a dictionary:
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
Brand_Car.pop("Ferrari")
print(Brand_Car) #Output: {'Ford': 1903, 'Bool': False, 'Colors': ['red', 'white', False]}
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
Brand_Car.popitem()
print(Brand_Car) #Output:  {'Ford': 1903, 'Ferrari': 1939, 'Bool': False}
#The del keyword removes the item with the specified key name:
del Brand_Car["Bool"]
print(Brand_Car) #Output:  {'Ford': 1903, 'Ferrari': 1939, 'Colors': ['red', 'white', False]}
#The del keyword can also delete the dictionary completely:
del Brand_Car
print(Brand_Car) #this will cause an error because "thisdict" no longer exists.
#The clear() method empties the dictionary:
Brand_Car.clear()
print(Brand_Car) #Output: {}


"""
Subtopic: Loop Dictionaries
1) You can loop through a dictionary by using a for loop.
2) When looping through a dictionary,
the return value are the keys of the dictionary, but there are methods to return the values as well.
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
for name in Brand_Car:
  print(name, end = " ") #Output: Ford Ferrari Bool Colors 
#Print all values in the dictionary, one by one:
for age in Brand_Car:
 	print(Brand_Car[age], end = " ") #Output: 1903 1939 False ['red', 'white', False] 
#You can also use the values() method to return values of a dictionary:
for age in Brand_Car.values():
  print(age, end = " ") #Output: 1903 1939 False ['red', 'white', False]
#You can use the keys() method to return the keys of a dictionary:
for name in Brand_Car.keys():
  print(name, end = " ") #Output: Ford Ferrari Bool Colors 
  #Loop through both keys and values, by using the items() method:
for name, age in Brand_Car.items():
  print(name, age, end = " ") #Output: Ford 1903 Ferrari 1939 Bool False Colors ['red', 'white', False]


"""
Subtopic: Copy a Dictionary
1) You cannot copy a dictionary simply by typing dict2 = dict1, because
dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
2) There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
Brand_Car = {
  "Ford" : 1903,
  "Ferrari" : 1939,
  "Bool" : False,
  "Colors": ["red", "white", False]
}
MyDict = Brand_Car.copy()
print(MyDict) #Output:{'Ford': 1903, 'Ferrari': 1939, 'Bool': False, 'Colors': ['red', 'white', False]}
#Make a copy of a dictionary with the dict() function:
MyDict = dict(Brand_Car)
print(MyDict)


"""
Subtopic: Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#Or, if you want to add three dictionaries into a new dictionary:
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"]) #Output: Tobias
#You can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
  print(x, end = " ")
  for y in obj:
    print(y + ':', obj[y], end = " ")
    #Output: child1
    #name: Emil year: 2004 child2
    #name: Tobias year: 2007 child3
    #name: Linus year: 2011 


"""
Subtopic: Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

clear()-----Removes all the elements from the dictionary
copy()-----Returns a copy of the dictionary
fromkeys()-----Returns a dictionary with the specified keys and value
get()-----Returns the value of the specified key
items()-----Returns a list containing a tuple for each key value pair
keys()-----Returns a list containing the dictionary's keys
pop()-----Removes the element with the specified key
popitem()-----Removes the last inserted key-value pair
setdefault()-----Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()-----Updates the dictionary with the specified key-value pairs
values()-----Returns a list of all the values in the dictionary
"""
