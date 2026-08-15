#read n
n=int(input("Enter a number:"))
org=n
rev=0
#reverse the number
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
#compare orginal and reverse
if org==rev:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
#output:
Enter a number:121
PALINDROME
    

    
