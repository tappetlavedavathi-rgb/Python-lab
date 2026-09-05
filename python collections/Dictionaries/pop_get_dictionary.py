d = {"a": 10, "b": 20, "c": 30}
key = input("Enter key to remove: ")
# Using pop()
if key in d:
    removed = d.pop(key)
    print("Removed value:",removed)
else:
    print("Key not found")
# Safely accessing a key using get()
key2 = input("Enter another key: ")
value = d.get(key2,"Key does not exist")
print(value)
print("Dictionary:",d)
#output:
Enter key to remove: a
Removed value: 10
Enter another key: b
20
Dictionary: {'b': 20, 'c': 30}
n
