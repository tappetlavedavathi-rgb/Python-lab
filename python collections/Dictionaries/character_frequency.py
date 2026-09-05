text=input("Enter a string: ")
frequency={}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequencies:")
for char, count in frequency.items():
    print(char, ":",count)
#output:
Enter a string: vedavathi
Character frequencies:
v : 2
e : 1
d : 1
a : 2
t : 1
h : 1
i : 1
