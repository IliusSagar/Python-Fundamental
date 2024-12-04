# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apple', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# print(fruits2, type(fruits2))

# Get valie
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)

