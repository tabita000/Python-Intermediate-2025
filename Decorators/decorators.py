"""
Assignment
Create a class-based decorator TimingDecorator that measures and prints the execution time of a function. 
Apply it to a computationally intensive function.

"""
# Time Decorator
import time
def timimg_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start: .4f} seconds")
        return result
    return wrapper

@timimg_decorator
def greet(name):
    print(f"Hello, {name}")
    
greet("Tabita!") 
print(" ")

# Modify the drive decorator
def drive_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__} with arguments {args} {kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Finished {func.__name__}")
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@drive_decorator
def car(make, model):
    print(f"Driving a {make} {model}")
    
car("Toyota", "Highlander") 
print(" ") 


# Implement caching decoder
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_decorator
def add(a, b):
    print("The result: ")
    return a + b
print(add(3, 3)) #first time adding
print(add(3, 3)) #second time adding. Second result coming from cache.
print("")


#Create a parameterized decorator
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def quack():
    print("Quack!")
    
quack() 
print("")  


#Assignment: Class-based Decorators
class TimingDecorator:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    
@TimingDecorator
def compute_factorial(n):
    total = 1
    for i in range(2, n + 1):
        total *= i
    return total
    
print(compute_factorial(10))
print(compute_factorial(20))

print("")        
       