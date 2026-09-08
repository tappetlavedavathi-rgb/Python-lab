s = input("Enter a string: ")
sub = input("Enter substring: ")
count = 0
first = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count = count + 1
        if first == -1:
            first = i
print("Find:", first)
print("Count:", count)
#output:
Enter a string: vedavathi
Enter substring: veda
Find: 0
Count: 1
