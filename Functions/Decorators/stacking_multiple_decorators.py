import time
from functools import wraps
# Task 2: Logging Decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
# Task 3: Timer Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result
    return wrapper
# Stacking both decorators
@log_call
@timer
def add(a, b):
    return a + b
# Test the function
result = add(10, 20)
print("Final result:", result)
#output:
Calling add args=(10, 20) kwargs={}
add took 0.000001 seconds
add returned 30
Final result: 30

