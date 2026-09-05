n=int(input("Enter number of items: "))
d={}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print("Keys:")
for key in d.keys():
    print(key)
print("Values:")
for value in d.values():
    print(value)
print("Key-Value pairs:")
for key, value in d.items():
    print(key, ":", value)
#output:
Enter number of items: 5
Enter key: 1
Enter value: 10
Enter key: 2
Enter value: 30
Enter key: 3
Enter value: 20
Enter key: 4
Enter value: 50
Enter key: 5
Enter value: 70
Keys:
1
2
3
4
5
Values:
10
30
20
50
70
Key-Value pairs:
1 : 10
2 : 30
3 : 20
4 : 50
5 : 70
