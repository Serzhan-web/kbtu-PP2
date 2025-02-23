"""
Subtopic: Python Lists
1. Lists are used to store multiple items in a single variable.
2. Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
3. Lists are created using square brackets:
"""
mylist = ['Python', 'Ruby', 'Go', 'Assembler', "Go"]
print(mylist) #Output: ['Python', 'Ruby', 'Go', 'Assembler', "Go"]

"""
List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

1. Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

2. Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

3. Allow Duplicates
Since lists are indexed, lists can have items with the same value:
"""

#To determine how many items a list has, use the len() function:
colors = ['Gray', 'White', 'Black']
print(len(colors)) #Output: 3

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"] #Type: String
list2 = [1, 5, 7, 9, 3] #Type: Integer
list3 = [True, False, False] #Type: Boolean
#A list can contain different data types:
strangeList= ["abc", 34, True, 40, "male"]

#It is also possible to use the list() constructor when creating a new list:
Numbers = list(((1,2), (0,5), (1,2))) # note the double round-brackets
print(Numbers) #Output: [(1, 2), (0, 5), (1, 2)]

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""


"""
Subtopic: Access List Items
1. List items are indexed and you can access them by referring to the index number:
2. The first item has index 0.
3. Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1], thislist[-1], thislist[-2]) #Output: banana cherry banana

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Output: ['cherry', 'orange', 'kiwi']
#The search will start at index 2 (included) and end at index 5 (not included).

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #Output: ['apple', 'banana', 'cherry', 'orange']

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #Output: ['orange', 'kiwi', 'melon']

#To determine if a specified item is present in a list use the in keyword:
OS = ['FreeBSD', 'Linux','Windows']
if "Lunix" in OS:
    print("Cool")
else:
    print("Bruh")


"""
Subtopic: Change List Items
To change the value of a specific item, refer to the index number:
"""
CPU = ["Intel", "Motorolla", "Windows"]
CPU[2] = "AMD"
print(CPU) #Output: ["Intel", "Motorolla", "AMD"]

"""
Change a Range of Item Values.
To change the value of items within a specific range, define a list with the new values,
and refer to the range of index numbers where you want to insert the new values:
"""
Games = ["Dark Souls 3", "Resident Evil Village", "Outlast", "Minecraft", "Elite Dangerous", "Far Cry Primal"]
Games[1:3] = ["GTA 5", "Need For Speed"]
print(Games) #Output: ["Dark Souls 3", "GTA 5", "Need For Speed", "Minecraft", "Elite Dangerous", "Far Cry Primal"]

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
Games = ["Dark Souls 3", "Resident Evil Village", "Outlast"]
Games[1:3] = ["GTA 5"]
print(Games) #Output: ["Dark Souls 3", "GTA 5", "Outlast"]

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
Games = ["Dark Souls 3", "Resident Evil Village", "Outlast"]
Games[1:2] = ["GTA 5", "Need For Speed"]
print(Games) #Output: ["Dark Souls 3", "GTA 5"]

"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
"""
Games = ["Dark Souls 3", "Resident Evil Village", "Outlast"]
Games.insert(2, "GTA 5")
print(Games) #Output: ["Dark Souls 3", "Resident Evil Village", "GTA 5", "Outlast"]


"""
Subtopic: Add List Items
To add an item to the end of the list, use the append() method:
"""
Anime = ["Naruto", "Death Note", "Demon Slayer"]
Anime.append("Van Piece")
print(Anime) #Output: ["Naruto", "Death Note", "Demon Slayer", "Van Piece"]

#To append elements from another list to the current list, use the extend() method:
fruits = ["apple", "banana", "cherry"]
tropical_fruits = ["mango", "pineapple", "papaya"]
fruits.extend(tropical_fruits)
print(fruits) #Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.):
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']


"""
Subtopic: Remove List Items.
The remove() method removes the specified item:
"""
Anime = ["Naruto", "Garry Potter", "Demon Slayer"]
Anime.remove("Garry Potter")
print(Anime) #Output: ["Naruto", Demon Slayer"]

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
Fruits = ["apple", "banana", "cherry", "banana", "kiwi"]
Fruits.remove("banana")
print(Fruits) #Output: ["apple", "cherry", "banana", "kiwi"]

"""
Remove Specified Index
The pop() method removes the specified index:
"""
Fruits = ["apple", "banana", "cherry"]
Fruits.pop(1)
print(Fruits) #Output: ["apple", "cherry"]

#If you do not specify the index, the pop() method removes the last item:
Fruits = ["apple", "banana", "cherry"]
Fruits.pop()
print(Fruits) #Output: ["apple", "banana"]

#The del keyword also removes the specified index:
Fruits = ["apple", "banana", "cherry"]
del Fruits[0]
print(Fruits) #Output: ["banana", "cherry"]

#The del keyword can also delete the list completely:
Fruits = ["apple", "banana", "cherry"]
del Fruits
print(Fruits) #Output:

"""
Clear the List.
The clear() method empties the list.
The list still remains, but it has no content.
"""
Fruits = ["apple", "banana", "cherry"]
Fruits.clear()
print(Fruits) #Output:


"""
Subtopic: Loop Lists
You can loop through the list items by using a for loop:
"""
Fruits = ["apple", "banana", "cherry"]
for i in Fruits:
  print(i, end=" ") #Output: apple banana cherry

"""
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
Fruits = ["apple", "banana", "cherry"]
for i in range(len(Fruits)):
  print(Fruits[i], end=" ") #Output: apple banana cherry

#You can loop through the list items by using a while loop:
Fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(Fruits):
  print(Fruits[i], end=" ") #Output: apple banana cherry
  i += 1

#List Comprehension offers the shortest syntax for looping through lists:
Fruits = ["apple", "banana", "cherry"]
[print(x) for x in Fruits]


"""
Subtopic: List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
Without list comprehension you will have to write a for statement with a conditional test inside:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)  #Output: ['apple', 'banana', 'mango']

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #Output: ['apple', 'banana', 'mango']

#The Syntax
newlist = [expression for item in iterable if condition == True]

#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist) #Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#The expression is the current item in the iteration, but it is also the outcome,
#which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]

#You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]


"""
Subtopic: Sort Lists
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
Fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
Fruits.sort()
print(Fruits) #Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sort the list numerically:
Numbers = [100, 50, 65, 82, 23]
Numbers.sort()
print(Numbers) #Output: [23, 50, 65, 82, 100]

#To sort descending, use the keyword argument reverse = True:
Fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
Fruits.sort(reverse = True)
print(Fruits) #Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#Sort the list descending:
Numbers = [100, 50, 65, 82, 23]
Numbers.sort(reverse = True)
print(Numbers) #Output: [100, 82, 65, 50, 23]

"""
Customize Sort Function.
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
"""
def myfunc(n):
  return abs(n - 50)

Numbers = [100, 50, 65, 82, 23]
Numbers.sort(key = myfunc)
print(Numbers) #Outptut: [50, 65, 23, 82, 100]

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
Fruits = ["banana", "Orange", "Kiwi", "cherry"]
Fruits.sort()
print(Fruits) #Output: ['Kiwi', 'Orange', 'banana', 'cherry']

"""
Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:
"""
Fruits = ["banana", "Orange", "Kiwi", "cherry"]
Fruits.sort(key = str.lower)
print(Fruits) #Output: ['banana', 'cherry', 'Kiwi', 'Orange']

"""
Reverse Order
The reverse() method reverses the current sorting order of the elements:
"""
Fruits = ["banana", "Orange", "Kiwi", "cherry"]
Fruits.reverse()
print(Fruits) #Output: ['cherry', 'Kiwi', 'Orange', 'banana']


"""
Subtopic: Copy Lists
1. You cannot copy a list simply by typing list2 = list1, because:
list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
2. You can use the built-in List method copy() to copy a list:
"""
Fruits = ["apple", "banana", "cherry"]
MyFruits = Fruits.copy()
print(MyFruits) #Output: ["apple", "banana", "cherry"]

#Another way to make a copy is to use the built-in method list():
Fruits = ["apple", "banana", "cherry"]
MyFruits = list(Fruits)
print(MyFruits) #Output: ["apple", "banana", "cherry"]

#You can also make a copy of a list by using the : (slice) operator:
ruits = ["apple", "banana", "cherry"]
MyFruits = Fruits[:]
print(MyFruits) #Output: ["apple", "banana", "cherry"]


"""
Subtopic: Join Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator:
"""
Letters = ["a", "b", "c"]
Digits = [1, 2, 3]
MyList = Letters + Digits
print(MyList) #Output: ['a', 'b', 'c', 1, 2, 3]

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
Letters = ["a", "b" , "c"]
Digits = [1, 2, 3]
for x in Digits:
  Letters.append(x)
print(Letters) #Output: ['a', 'b', 'c', 1, 2, 3]

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
Letters = ["a", "b" , "c"]
Digits = [1, 2, 3]
Letters.extend(Digits)
print(Letters)


"""
Subtopic: List Methods
Python has a set of built-in methods that you can use on lists.

append()---Adds an element at the end of the list
clear()---Removes all the elements from the list
copy()---Returns a copy of the list
count()---Returns the number of elements with the specified value
extend()---Add the elements of a list (or any iterable), to the end of the current list
index()---Returns the index of the first element with the specified value
insert()---Adds an element at the specified position
pop()---Removes the element at the specified position
remove()---Removes the item with the specified value
reverse()---Reverses the order of the list
sort()---Sorts the list
"""
