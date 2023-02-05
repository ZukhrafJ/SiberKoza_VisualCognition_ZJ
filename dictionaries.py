# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictionary 

person_zj = {
    'first_name': 'John',
    'last_name': 'levis',
    'age': 30
}

# Use constructor 

#person2 = dict(first_name='sara', last_name='Ali')

# Get value 
print(person_zj['first_name'])

# Add key value
person_zj['phone'] = '123-123-123'

# Get dict keys
print(person_zj.keys())

# Get dict items
print(person_zj.items())

# Copy dict 
person2 = person_zj.copy()
person2['city'] = 'islamabad'

# Remove item 
del(person_zj['age'])

person2.pop('phone')
# Clear 

person2.clear()

# Get length
print(len(person_zj))

# List of dict 
people = [
    {'name': 'zuk', 'age': '25'},
     {'name': 'kevin', 'age': '30'}
]

print(person_zj)
#print(person_zj.get('last_name'))
print(person2)
print(people)
