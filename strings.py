# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Zuk'
age = 30

# Concatenate
print('Hello, my name is ' , name, 'and I am' , str(age))

# String Formatting

# Arguements by position

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods
s = 'hello world'

# Capitalize string 

print(s.capitalize())
