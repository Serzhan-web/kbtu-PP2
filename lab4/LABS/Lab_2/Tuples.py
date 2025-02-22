"""
Subtopic: Python Tuples
1. Tuples are used to store multiple items in a single variable.
2. A tuple is a collection which is ordered and unchangeable.
3. Tuples are written with round brackets.
"""
Movie = ("Garry Potter", "Terminator", "Star Wars")
print(Movie) #Output: ("Garry Potter", "Terminator", "Star Wars")

"""
1. Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
2. Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
3. Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
4. Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""
Movie = ("Garry Potter", "Terminator", "Star Wars", "Interstellar", "Terminator")
print(Movie[0], Movie[1], Movie[-1]) #Output: Garry Potter Terminator Terminator
#To determine how many items a tuple has, use the len() function:
print(len(Movie)) #Output: 5

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple:
Fruit = ("apple",)
#NOT a tuple:
Fruit = ("apple")

#Tuple items can be of any data type:
Fruits = ("apple", "banana", "cherry")
Digits = (1, 5, 7, 9, 3)
Logics = (True, False, False)
#A tuple can contain different data types:
MyTuple = ("Intel", 42, True, 2077, "Interstellar")

#From Python's perspective, tuples are defined as objects with the data type 'tuple':
Fruits = ("apple", "banana", "cherry")
print(type(Fruits)) #Output: <class 'tuple'>

#It is also possible to use the tuple() constructor to make a tuple:
Fruits = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(Fruits) 


"""
Subtopic: Access Tuple Items
You can access the tuple element, just like with a list;)
"""


"""
Subtopic: Update Tuples
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds. You can convert the tuple into a list, change the list, and convert the list back into a tuple:
"""
Fruits_Tuple = ("apple", "banana", "cherry")
Fruits_List = list(Fruits_Tuple)
Fruits_List[1] = "kiwi"
Fruits_Tuple = tuple(Fruits_List)
print(Fruits_Tuple) #Output: ("apple", "kiwi", "cherry")

"""
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple,
you can convert it into a list, add your item(s), and convert it back into a tuple.
"""
Fruits = ("apple", "banana", "cherry")
Fruits_List = list(Fruits)
Fruits_List.append("orange")
Fruits = tuple(Fruits_List)

"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples,
so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""
Fruits = ("apple", "banana", "cherry")
Fruits_2 = ("orange",)
Fruits += Fruits_2
print(Fruits) #Output: ('apple', 'banana', 'cherry', 'orange')

"""
Tuples are unchangeable, so you cannot remove items from it,
but you can use the same workaround as we used for changing and adding tuple items:
"""
Fruits = ("apple", "banana", "cherry")
Fruits_List = list(Fruits)
Fruits_List.remove("apple")
Fruits = tuple(Fruits_List)
print(Fruits) #Output: ('banana', 'cherry')

#Or you can delete the tuple completely:
Fruits = ("apple", "banana", "cherry")
del Fruits
print(Fruits) #this will raise an error because the tuple no longer exists


"""
Subtopic: Unpack Tuples
When we create a tuple, we normally assign values to it. This is called "packing" a tuple,
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
"""
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) #Output: apple
print(yellow) #Output: banana
print(red) #Output: cherry

"""
Using Asterisk*
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will be assigned to the variable as a list:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green, yellow, red) #Output: apple banana ['cherry', 'strawberry', 'raspberry']

"""
If the asterisk is added to another variable name than the last,
Python will assign values to the variable until the number of values left matches the number of variables left:
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green, tropic, red) #Output: apple ['mango', 'papaya', 'pineapple'] cherry


"""
Subtopis: Loop Tuples
You can loop through the tuple items by using a for loop.
Iterate through the items and print the values:
"""
Fruits = ("apple", "banana", "cherry")
for item in Fruits:
  print(item, end = ' ')

#Print all items by referring to their index number:
Fruits = ("apple", "banana", "cherry")
for i in range(len(Fruits)):
  print(Fruits[i])

#Print all items, using a while loop to go through all the index numbers:
Fruits = ("apple", "banana", "cherry")
i = 0
while i < len(Fruits):
  print(Fruits[i])
  i = i + 1


"""
Subtopic: Join Two Tuples
To join two or more tuples you can use the + operator:
"""
Fruits = ("a", "b" , "c")
Numbers = (1, 2, 3)
MyTuple = Fruits + Numbers
print(MyTuple) #Output: ('a', 'b', 'c', 1, 2, 3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
Fruits = ("apple", "banana", "cherry")
More_Fruits = Fruits * 2
print(More_Fruits) #Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


"""
Subtopic: Tuple Methods
Python has two built-in methods that you can use on tuples:

1) count()	Returns the number of times a specified value occurs in a tuple
2) index()	Searches the tuple for a specified value and returns the position of where it was found
"""
