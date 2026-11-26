def greet(name):
    print("Hello", name, "welcome to the program")

greet("Evelyne Njambi")

def evenOdd(x):
    if (x %2 ==0):
        return "Even"
    else: 
        return "Odd"
print(evenOdd(16))
print(evenOdd(9))

#Keyword Arguments
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)


print("Case-2:")
nameAge(27, "Olivia")
print()

#Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-keyword arguments: ")
    for arg in args: 
        print(arg)

    print("Keyword arguments: ")
    for key, value in kwargs.items():
        print(f"{key} == {value}")
myFun("Hey", "Welcome", first='Geeks', mid ='for', last ='Geeks')        
print()

# Recursion
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))
print()

def mySum(*args):
    return sum(args)
print(mySum(12,8,20,35))
print()

def fun(*args):
    return sum(args)

print(fun(5, 10, 1,4))
print()

# **Kwargs
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}. {value}")
myFun(a= "Reading", b="Exploring", c="Coding")
print()

def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="Alice", Age=25, City="New York"))
print()

a = "GreeksforGeeks"
upper = lambda x: x.upper()
print(upper(a))
print()

factor = lambda a,c,b : a*b*c
print(factor(1,3,6))

# Decorators
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()

# def welcome(name):
#     print(f"Hello {name}")

# Add a desorator to the welcome function
# def decorator(func):
#     def wrapper():
#         print("This is an upgraded version for the site")
#         func()
#         print("You can now interact with the premium content in the freemium version for this month!")
#     return wrapper
# @decorator 
# def welcome(name):
#     print(f"Hello {name}")
    
# welcome("Njambi")

# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet 
print(say_hi("Alex")) 

# Passing a function as an argument
def apply(f, v):
    return f(v)
res = apply(say_hi, "Elon")
print(res) 

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))

# Method decorator
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# Class decorator
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)

# Built-in decorators
# 1. @static
class MathOperations:
    @staticmethod
    def add(x,y):
        return x + y
res = MathOperations.add(5,3)
print(res)

    # 2. @classmethod- Defines the method  that operates on the class itself
class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

    # 3. @property- used to define a method as a property, which allows to access it like an attribute. 
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)

