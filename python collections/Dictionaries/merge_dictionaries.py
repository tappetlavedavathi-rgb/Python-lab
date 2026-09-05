dict1={"a": 10, "b": 20}
dict2={"c": 30, "d": 40}
# Using update()
merged1 = dict1.copy()
merged1.update(dict2)
print("Using update():",merged1)
# Using | operator
merged2 = dict1 | dict2
print("Using | operator:",merged2)
#output:
Using update(): {'a': 10, 'b': 20, 'c': 30, 'd': 40}
Using | operator: {'a': 10, 'b': 20, 'c': 30, 'd': 40}

