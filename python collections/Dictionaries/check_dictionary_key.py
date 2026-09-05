d ={"name": "Vedavathi", "age": 18, "branch": "CSE"}
key=input("Enter key to search: ")
if key in d:
    print("Value:", d[key])
else:
    print("Key does not exist")
#output:
Enter key to search: name
Value: Vedavathi
