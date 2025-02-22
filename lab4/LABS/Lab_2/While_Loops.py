"""
Topic: Python While Loops
With the while loop we can execute a set of statements as long as a condition is true.
"""
Num = 42
while Num < 2077:
  print(Num)
  Num += 1
#Note: remember to increment i, or else the loop will continue forever.

"""
The break Statement
With the break statement we can stop the loop even if the while condition is true:
"""
Num = 42
while Num < 2077:
  print(Num)
  if Num == 1969:
    break
  Num += 1

"""
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
"""
Num = 42
while Num < 2077:
  Num += 1
  if Num == 1939:
    continue
  print(Num)

"""
The else Statement
With the else statement we can run a block of code once when the condition no longer is true:
"""
Num = 42
while Num < 2077:
  print(Num)
  Num += 1
else:
  print("Num is no longer less than 2077")
