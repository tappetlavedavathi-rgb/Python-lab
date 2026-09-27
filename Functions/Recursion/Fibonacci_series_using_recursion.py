def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("First 15 Fibonacci terms:")
for i in range(15):
    print(fibonacci(i), end=" ")
print()
print("Fibonacci(10):", fibonacci(10))
#output:
First 15 Fibonacci terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
Fibonacci(10): 55

