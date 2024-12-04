# A varicable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docastring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
    - Variable names are case sensative (name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # floar
# name = 'Jhon'   # str
# is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Jhon', True)

# Basic Math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

# print(x, y, name, is_cool, a)
# print(type(x))
print(type(z), z)