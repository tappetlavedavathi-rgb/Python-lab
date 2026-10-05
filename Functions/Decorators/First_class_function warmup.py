# (a) Assigning a function to a new variable
def greet(name):
    return "Hello, " + name
new_greet = greet
print(new_greet("Alice"))
# (b) Passing a function as an argument
def calculate(func, a, b):
    return func(a, b)
def add(a, b):
    return a + b
print(calculate(add, 10, 20))
# (c) Returning a function from another function
def create_multiplier():
    def multiply(x):
        return x * 2
    return multiply
double = create_multiplier()
print(double(5))
#output:
Hello, Alice
30
10

