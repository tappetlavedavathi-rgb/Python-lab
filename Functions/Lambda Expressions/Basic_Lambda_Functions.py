square = lambda x: x ** 2
# (b) Check if a number is even
is_even = lambda x: x % 2 == 0
# (c) Find the larger of two numbers
larger = lambda x, y: x if x > y else y
print("Square:", square(5))
print("Is Even:", is_even(8))
print("Larger:", larger(10, 7))
#output:
Square: 25
Is Even: True
Larger: 10
