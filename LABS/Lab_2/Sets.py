"""
Subtopic: Python Sets
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets:
"""
Fruits = {"apple", "banana", "cherry"}
print(Fruits) #Output: {"apple", "banana", "cherry"}

'''
1) Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.
2) Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
3) Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.
4) Duplicates Not Allowed
Sets cannot have two items with the same value:
'''
Fruits = {"apple", "banana", "cherry", "apple"}
print(Fruits) #Output: {"banana", "cherry", "apple"}

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
Fruits = {"apple", "banana", "cherry", True, 1, 2}
print(Fruits) #Output: {True, 2, 'banana', 'cherry', 'apple'}

#The values False and 0 are considered the same value in sets, and are treated as duplicates:
Fruits = {"apple", "banana", "cherry", False, True, 0}
print(Fruits) #Output: {False, True, 'cherry', 'apple', 'banana'}

#To determine how many items a set has, use the len() function:
Fruits = {"apple", "banana", "cherry"}
print(len(Fruits)) #Output: 3

#Set Items - Data Types
#Set items can be of any data type:
Set_1 = {"apple", "banana", "cherry"}
Set_2 = {1, 5, 7, 9, 3}
Set_3 = {True, False, False}

#A set can contain different data types:
Set_1 = {"Ferrari", 2077, True, 42, "John"}

#From Python's perspective, sets are defined as objects with the data type 'set':
Fruits = {"apple", "banana", "cherry"}
print(type(Fruits)) #Output: <class 'set'>

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
Numbers = [1,1,1,1,1,42,1,2077]
Numbers_Set = set(Numbers)
print(Numbers_Set) #Output: {1, 42, 2077}


"""
Subtopic: Access Set Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword:
"""
Fruits = {"apple", "banana", "cherry"}
for item in Fruits:
  print(item, end = " ") #Output: apple cherry banana 

#Check if "banana" is present in the set:
Fruits = {"apple", "banana", "cherry"}
print("banana" in Fruits) #Output: True
print("banana" not in Fruits) #Output: False


"""
Subtopic: Add Set Items
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method:
"""
Fruits = {"apple", "banana", "cherry"}
Fruits.add("orange")
print(Fruits) #Output: {'orange', 'banana', 'apple', 'cherry'}

#To add items from another set into the current set, use the update() method.
Fruits = {"apple", "banana", "cherry"}
Tropical = {"pineapple", "mango", "papaya"}
Fruits.update(Tropical)
print(Tropical) #Output:{'mango', 'pineapple', 'papaya'}
print(Fruits) #Output: {'cherry', 'banana', 'apple', 'papaya', 'pineapple', 'mango'}

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.):
Fruits = {"apple", "banana", "cherry"}
Fruits_List = ["kiwi", "orange"]
Fruits.update(Fruits_List)
print(Fruits) #Output: {'banana', 'cherry', 'apple', 'orange', 'kiwi'}


"""
Subtopic: Remove Set Items
To remove an item in a set, use the remove(), or the discard() method.
Remove "5" by using the remove() method:
"""
Numbers = {42, 2077, 6800, 8088, 5}
Numbers.remove(5)
print(Numbers) #Output: {42, 6800, 8088, 2077}
#If the item to remove does not exist, remove() will raise an error.

#Remove "5" by using the discard() method:
Numbers = {42, 2077, 6800, 8088, 5}
Numbers.discard(5)
print(Numbers) #Output: {42, 6800, 8088, 2077}
#If the item to remove does not exist, discard() will NOT raise an error.

"""
1) You can also use the pop() method to remove an item,
but this method will remove a random item, so you cannot be sure what item that gets removed.
2) The return value of the pop() method is the removed item.
"""
Numbers = {42, 2077, 6800, 8088}
Pop_Number = Numbers.pop()
print(Pop_Number) #Output: 6800
print(Numbers) #Output: {8088, 42, 2077}

#The clear() method empties the set:
Numbers = {42, 2077, 6800, 8088}
Numbers.clear()
print(Numbers) #Output: set()

#The del keyword will delete the set completely:
Numbers = {42, 2077, 6800, 8088}
del Numbers
print(Numbers)  #this will raise an error because the set no longer exists


"""
Subtopic: Join Sets
There are several ways to join two or more sets in Python:
1) The union() and update() methods joins all items from both sets:
"""
Letters = {"a", "b", "c"}
Numbers = {1, 2, 3}
MySet = Letters.union(Numbers)
print(MySet) #Output: {3, 'c', 2, 'b', 'a', 1}

#You can use the | operator instead of the union() method, and you will get the same result.
Movie = {"Interstellar", "Terminator", "Avatar"}
Numbers = {6800, 2077, 42}
Anime = {"Naruto", "My hero academia"}
Game = {"Half Life 2", "WOW 3", "FNAF"}
MySet = Movie | Numbers | Anime |Game
print(MySet) #Output: {'Avatar', 'My hero academia', 'WOW 3', 'Interstellar', 42, 'Half Life 2', 'Terminator', 6800, 'Naruto', 2077, 'FNAF'}

#Join multiple sets with the union() method:
Movie = {"Interstellar", "Terminator", "Avatar"}
Numbers = {6800, 2077, 42}
Anime = {"Naruto", "My hero academia"}
Game = {"Half Life 2", "WOW 3", "FNAF"}
MySet = Movie.union(Numbers, Anime, Game)
print(MySet) #Output: {'Avatar', 'My hero academia', 'WOW 3', 'Interstellar', 42, 'Half Life 2', 'Terminator', 6800, 'Naruto', 2077, 'FNAF'}

#The intersection() method will return a new set, that only contains the items that are present in both sets.
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits.intersection(IT_Company)
print(MySet) #Output: {'apple'}

#You can use the & operator instead of the intersection() method, and you will get the same result:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits & IT_Company
print(MySet) #Output: {'apple'}

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
Fruits.intersection_update(IT_Company)
print(Fruits) #Output: {'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0:
Fruits = {"apple", 1,  "banana", 0, "cherry"}
IT_Company = {False, "google", 1, "apple", 2, True}
MySet = Fruits.intersection(IT_Company)
print(MySet) #Output: {False, True, 'apple'}

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits.difference(IT_Company)
print(MySet) #Output: {'banana', 'cherry'}

#You can use the "-" operator instead of the difference() method, and you will get the same result.
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits - IT_Company
print(MySet) #Output: {'banana', 'cherry'}

#Use the difference_update() method to keep the items that are not present in both sets:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
Fruits.difference_update(IT_Company)
print(Fruits) #Output: {'apple'}

#The symmetric_difference() method will keep only the elements that are NOT present in both sets:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits.symmetric_difference(IT_Company)
print(MySet) #Output: {'google', 'banana', 'microsoft', 'cherry'}

#You can use the ^"" operator instead of the symmetric_difference() method, and you will get the same result:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
MySet = Fruits ^ IT_Company
print(MySet) #Output: {'google', 'banana', 'microsoft', 'cherry'}

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
Fruits = {"apple", "banana", "cherry"}
IT_Company = {"google", "microsoft", "apple"}
Fruits.symmetric_difference_update(IT_Company)
print(Fruits) #Output: {'google', 'banana', 'microsoft', 'cherry'}


"""
Subtopic: Set Methods
Python has a set of built-in methods that you can use on sets:

1) add()-------Adds an element to the set
2) clear()------Removes all the elements from the set
3) copy()-------Returns a copy of the set
4) difference()-----	"-" Returns a set containing the difference between two or more sets
5) difference_update()------- "-="	Removes the items in this set that are also included in another, specified set
6) discard()-------Remove the specified item
7) intersection()------- "&"	Returns a set, that is the intersection of two other sets
8) intersection_update()------- "&="	Removes the items in this set that are not present in other, specified set(s)
9) isdisjoint()-------Returns whether two sets have a intersection or not
10) issubset()------ "<="	Returns whether another set contains this set or not
 	                   "<"	Returns whether all items in this set is present in other, specified set(s)
11) issuperset()------ ">="	Returns whether this set contains another set or not
 	                      ">"	Returns whether all items in other, specified set(s) is present in this set
12) pop()-------Removes an element from the set
13) remove()------Removes the specified element
14) symmetric_difference()------ "^"	Returns a set with the symmetric differences of two sets
15) symmetric_difference_update()------- "^="	Inserts the symmetric differences from this set and another
16) union()-------- "|"	Return a set containing the union of sets
17) update()-------- "|="	Update the set with the union of this set and others
"""
