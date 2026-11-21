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

#Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-keyword arguments: ")
    for arg in args:
        print(arg)

    print("Keyword arguments: ")
    for key, value in kwargs.items():
        print(f"{key} == {value}")
        