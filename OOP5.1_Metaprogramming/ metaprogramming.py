"""
OOP 5.1 - Metaprogramming
This program creates a class dynamically using type().
The new class has two methods: greet() and bye().
"""

# Define two small functions that will become methods
def greet(self):
    return "Hello from dynamic class!"

def bye(self):
    return "Goodbye!"

# Create the class using type()
MyDynamicClass = type("MyDynamicClass", (object,), {"greet": greet, "bye": bye})

# Make an object from the new class
obj = MyDynamicClass()

# Test the methods
print(obj.greet())
print(obj.bye())
