#Subtopic: Python Strings

#'Hello' is the same as "Hello".
print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
university = "KBTU"
print(university)

#You can assign a multiline string to a variable by using three quotes:
#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
some_str = "Hello, World!"
print(some_str[0]) #Output: H

#Looping Through a String
for x in "KBTU":
  print(x) #Output: K/n B/n T/n U/n

#String Length
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!
print("free" in txt)
#Print only if "free" is present:
if "free" in txt:
  print("Yes, 'free' is present.")
else:
    print("bruh")
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print('Seriy' not in txt) #Output: True


"""
Subtopic: Slicing Strings
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
#Slicing
x = "Hello, KBTU!"
print(x[2:5]) #Output: llo

#Slice From the Start
x = "Hello, KBTU!"
print(x[:5]) #Output: Hello

#Slice To the End
x = "Hello, KBTU!"
print(x[2:]) #Output: llo, KBTU!

#Negative Indexing
x = "Hello, KBTU!"
print(x[-5:-2]) #Output: KBT


"""
Subtopic: Modify Strings
Python has a set of built-in methods that you can use on strings.
"""
#The upper() method returns the string in upper case:
a = "Intel"
print(a.upper()) #Output: INTEL
#The lower() method returns the string in lower case:
b = "AMD"
print(b.lower()) #Output: amd
#The strip() method removes any whitespace from the beginning or the end:
c = "    Motorolla    "
print(c.strip()) #Output: "Motorolla"
c = c.strip()
#The replace() method replaces a string with another string:
a = "I'm Guy!"
print(a.replace("u", "a"))
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # Output: ['Hello', ' World!']


"""
Subtopic: Concatenate Strings
To concatenate, or combine, two strings you can use the + operator.
"""
a = "Hello"
b = "World"
c = a + b
print(c) #Output: HelloWorld
#To add a space between them, add a " ":
print(a +" " +  b, "; ", c) #Output: Hello World; HelloWorld


"""
Subtopic: Format - Strings
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
"""
age = 42
txt = "My name is John, I am " + age
print(txt) #Output: My name is John, I am 42
"""
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal,
and add curly brackets {} as placeholders for variables and other operations.
"""
#Create an f-string:
age = 42
txt = f"My name is John, I am {age}"
print(txt) #Output: My name is John, I am 42

#Add a placeholder for the price variable:
price = 42
txt = f"The price is {price} dollars"
print(txt) #Output: The price is 42 dollars

#Display the price with 2 decimals:
price = 2077
txt = f"The price is {price:.2f} dollars"
print(txt) #Output: The price is 2077.00 dollars

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {42 * 2077} dollars"
print(txt) #Output: The price is 87234 dollars


"""
Subtopic: Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
"""
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north." #INCORRECT
#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north." #CORRECT

"""
Other escape characters used in Python:
\'---Single Quote	
\\---Backslash	
\n---New Line	
\r---Carriage Return	
\t---Tab	
\b---Backspace	
\f---Form Feed	
\ooo---Octal value	
\xhh---Hex value
"""


"""
Subtopic: String Methods
Python has a set of built-in methods that you can use on strings.
Note: All string methods return new values. They do not change the original string.

capitalize()-------Converts the first character to upper case
casefold()-------Converts string into lower case
center()-------Returns a centered string
count()-------Returns the number of times a specified value occurs in a string
encode()-------Returns an encoded version of the string
endswith()-------Returns true if the string ends with the specified value
expandtabs()-------Sets the tab size of the string
find()-------Searches the string for a specified value and returns the position of where it was found
format()-------Formats specified values in a string
format_map()-------Formats specified values in a string
index()-------Searches the string for a specified value and returns the position of where it was found
isalnum()-------Returns True if all characters in the string are alphanumeric
isalpha()-------Returns True if all characters in the string are in the alphabet
isascii()-------Returns True if all characters in the string are ascii characters
isdecimal()-------Returns True if all characters in the string are decimals
isdigit()-------Returns True if all characters in the string are digits
isidentifier()-------Returns True if the string is an identifier
islower()-------Returns True if all characters in the string are lower case
isnumeric()-------Returns True if all characters in the string are numeric
isprintable()-------Returns True if all characters in the string are printable
isspace()-------Returns True if all characters in the string are whitespaces
istitle()-------Returns True if the string follows the rules of a title
isupper()-------Returns True if all characters in the string are upper case
join()-------Joins the elements of an iterable to the end of the string
ljust()-------Returns a left justified version of the string
lower()-------Converts a string into lower case
lstrip()-------Returns a left trim version of the string
maketrans()-------Returns a translation table to be used in translations
partition()-------Returns a tuple where the string is parted into three parts
replace()-------Returns a string where a specified value is replaced with a specified value
rfind()-------Searches the string for a specified value and returns the last position of where it was found
rindex()-------Searches the string for a specified value and returns the last position of where it was found
rjust()-------Returns a right justified version of the string
rpartition()-------Returns a tuple where the string is parted into three parts
rsplit()-------Splits the string at the specified separator, and returns a list
rstrip()-------Returns a right trim version of the string
split()-------Splits the string at the specified separator, and returns a list
splitlines()-------Splits the string at line breaks and returns a list
startswith()-------Returns true if the string starts with the specified value
strip()-------Returns a trimmed version of the string
swapcase()-------Swaps cases, lower case becomes upper case and vice versa
title()-------Converts the first character of each word to upper case
translate()-------Returns a translated string
upper()-------Converts a string into upper case
zfill()-------Fills the string with a specified number of 0 values at the beginning
"""
