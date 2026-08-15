#read n
n=int(input("Enter a number:"))
rev=0
#reversing
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print("Reversed number=", rev)
#output:
Enter a number:2234
Reversed number= 4322

