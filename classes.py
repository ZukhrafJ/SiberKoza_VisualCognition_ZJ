# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create a class
class zukuser:
    # Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'my name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age +=1

 # extend class
 #
class customer(zukuser):
        # Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance 

    def greeting(self):
        return f'my name is {self.name} and I am {self.age} and my balance is {self.balance}'
# initialize user object 

bradz = zukuser('brad lim', 'bradz@ymail.com' , 37)

# initialize customer 

jany = customer('jany john', 'jane@gmail.com', 25)
jany.set_balance(500)
bradz.has_birthday()
print(bradz.greeting())
print(jany.greeting())

