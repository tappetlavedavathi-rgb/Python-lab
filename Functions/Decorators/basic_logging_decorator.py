# Basic logging decorator
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
# Applying the decorator
@log_call
def add(a, b):
    return a + b
# Test the function
result = add(10, 20)

print("Final result:", result)
#output:
Calling add args=(10, 20) kwargs={}
add returned 30
Final result: 30

