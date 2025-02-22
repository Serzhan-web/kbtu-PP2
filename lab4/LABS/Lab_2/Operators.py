"""
Python Operators
Operators are used to perform operations on variables and values.
In the example below, we use the + operator to add together two values:
"""
print(42+2077) #Output: 2119

"""
Python divides the operators in the following groups:
1) Arithmetic operator:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus (remainder of division)
//  Floor division (integer division)
**  Exponentiation (power)

2) Assignment Operators:
=   Assign a value
+=  Add and assign (x += y → x = x + y)
-=  Subtract and assign (x -= y → x = x - y)
*=  Multiply and assign (x *= y → x = x * y)
/=  Divide and assign (x /= y → x = x / y)
%=  Modulus and assign (x %= y → x = x % y)
//= Floor division and assign (x //= y → x = x // y)
**= Exponentiation and assign (x **= y → x = x ** y)
&=  Bitwise AND and assign
|=  Bitwise OR and assign
^=  Bitwise XOR and assign
>>= Right shift and assign
<<= Left shift and assign

3) Comparison operators:
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to

4) Logical operators:
and   Logical AND (x and y → True if both x and y are True)
or    Logical OR (x or y → True if either x or y is True)
not   Logical NOT (not x → True if x is False)

5) Identity operators:
is       Returns True if both objects are the same (x is y)
is not   Returns True if objects are different (x is not y)

6) Membership operators:
in       Returns True if the value is in the sequence (x in y)
not in   Returns True if the value is not in the sequence (x not in y)

7) Bitwise operators:
&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR (exclusive OR)
~   Bitwise NOT (inverts all bits)
<<  Left shift (shifts bits to the left)
>>  Right shift (shifts bits to the right)
"""

#Operator precedence describes the order in which operations are performed.
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) #Output: 0
print((6+3) - 6+3) #Output: 6

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3) #Output: 115

'''
The precedence order is described in the table below, starting with the highest precedence at the top:
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
== !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''

#If two operators have the same precedence, the expression is evaluated from left to right.
#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
print(5 + 4 - 7 + 3) #Output: 5
