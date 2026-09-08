s = input("Enter a string: ")
for ch in set(s):
    if s.count(ch) > 1:
        print(ch, ":", s.count(ch))
#output:
Enter a string: vedavathi
a : 2
v : 2
