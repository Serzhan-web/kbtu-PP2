"""
Specify a Variable Type
Casting in python is therefore done using constructor functions:

1. int() - constructs an integer number from an integer literal,
a float literal (by removing all decimals), or a string literal (providing the string represents a whole number).

2. float() - constructs a float number from an integer literal,
a float literal or a string literal (providing the string represents a float or an integer).

3. str() - constructs a string from a wide variety of data types,
including strings, integer literals and float literals.
"""

#Examples:
#Integers
x = int(42)   # x will be 42
y = int(2077.8) # y will be 2077
z = int("3.999999999999999") # z will be 3

#FLoats
x = float(42)     # x will be 42.0
y = float(2077.8)   # y will be 2077.8
z = float("3.999999999999999")   # z will be 3.999999999999999
w = float("3,1415926535") # w will be 3,1415926535

#Strings
x = str("Motorolla 6800") # x will be 'Motorolla 6800'
y = str(42)    # y will be '42'
z = str(2077.2077)  # z will be '2077.2077'
