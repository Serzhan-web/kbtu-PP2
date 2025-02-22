"""
Topic: Python For Loops
1) A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
2) This is less like the for keyword in other programming languages,
and works more like an iterator method as found in other object-orientated programming languages.
3) With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
Fruits = ["apple", "banana", "cherry"]
for x in Fruits:
  print(x, end = " ") #Output: apple banana cherry
  
#Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x, end = " ") #Output: b a n a n a

#With the break statement we can stop the loop before it has looped through all the items:
Fruits = ["apple", "banana", "cherry"]
for x in Fruits:
  print(x) #Output: apple
  if x == "banana":
    break

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
Fruits = ["apple", "banana", "cherry"]
for x in Fruits:
  if x == "banana":
    continue
  print(x, end = " ") #Output: apple cherry

"""
The range() Function
1) To loop through a set of code a specified number of times, we can use the range() function,
2) The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""
for i in range(43):
    print(i, end=" ")
print() #Output: 0 1 2 ... 39 41 42
#Note that range(43) is not the values of 0 to 43, but the values 0 to 42.

"""
The range() function defaults to 0 as a starting value,
however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
"""
for x in range(2, 6):
  print(x, end = " ") #Output: 2 3 4 5

"""
The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
"""
for x in range(2, 30, 3):
  print(x, end = " ") #Output: 2 5 8 11 14 17 20 23 27

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Note: The else block will NOT be executed if the loop is stopped by a break statement.

#One more example:
Numbers = [i for i in range(1,2077 + 1)]
print(len(Numbers)) #Output: 2077

"""
Nested Loops like an Matrix
1) A nested loop is a loop inside a loop.
2) The "inner loop" will be executed one time for each iteration of the "outer loop":
"""
Colors = ["red", "big", "tasty"]
Fruits = ["apple", "banana", "cherry"]
for x in Colors:
  for y in Fruits:
    print(x, y, end = " ") #Output: red apple red banana red cherry big apple big banana big cherry tasty apple tasty banana tasty cherry 

#One more example:
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end="\t")
    print()
"""
Output will look like an Multiplication table up to ten:
1	  2	  3	  4	  5	  6	  7	  8	  9	
2	  4	  6	  8	 10	 12	 14	 16	 18	
3	  6	  9	 12	 15	 18	 21	 24	 27
4	  8	 12	 16	 20	 24	 28	 32	 36	
5	 10	 15	 20	 25	 30	 35	 40	 45	
6	 12	 18	 24	 30	 36	 42	 48	 54	
7	 14	 21	 28	 35	 42	 49	 56	 63	
8	 16	 24	 32	 40	 48	 56	 64	 72	
9	 18	 27	 36	 45	 54	 63	 72	 81
"""

"""
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the "pass" statement to avoid getting an error.
"""
for x in [0, 1, 2]:
  pass
