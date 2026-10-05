# Parameterised decorator
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
# Repeat the greeting 3 times
@repeat(3)
def greet():
    print("Hello, welcome to Python!")
# Call the function
greet()
#output:
Hello, welcome to Python!
Hello, welcome to Python!
Hello, welcome to Python!

