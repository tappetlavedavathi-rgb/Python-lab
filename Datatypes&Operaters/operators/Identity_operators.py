list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
print(id(list1))
print(id(list2))
print(id(list3))
#output:
True
False
True
2175583186816
2175583177792
2175583186816
