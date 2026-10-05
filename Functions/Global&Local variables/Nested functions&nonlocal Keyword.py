def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
# Create the counter
counter = make_counter()
# Call the returned function multiple times
print(counter())
print(counter())
print(counter())
print(counter())
#output:
1
2
3
4
