numbers = (10, 20, 30, 40)
try:
    numbers[0] = 100
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
#output:
Error: 'tuple' object does not support item assignment
Tuples are immutable and cannot be modified.
