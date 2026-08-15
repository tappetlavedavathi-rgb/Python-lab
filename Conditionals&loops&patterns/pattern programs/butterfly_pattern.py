#read n
n=int(input("Enter n value:"))
#upper part
for i in range(1,n+1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
#lower part
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
#output:
Enter n value:4
*      *
**    **
***  ***
********
***  ***
**    **
*      *


    
