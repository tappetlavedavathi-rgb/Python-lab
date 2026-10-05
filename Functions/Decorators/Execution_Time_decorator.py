import time
# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result
    return wrapper
# Computationally heavy function
@timer
def calculate_sum():
    total = 0
    for i in range(1, 10000000):
        total += i
    return total
# Call the function
result = calculate_sum()
print("Sum:", result)
#output:
calculate_sum took 0.517084 seconds
Sum: 49999995000000

