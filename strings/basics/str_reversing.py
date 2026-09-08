s=input("Enter a string:");
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print("Reverse without using slicing:", rev)
print("Reverse with slicing:",s[::-1])
#output:

