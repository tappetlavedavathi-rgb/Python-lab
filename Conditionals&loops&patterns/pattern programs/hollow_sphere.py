#read n
n=int(input("Enter n value:"))
#print hollow sphere
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
#output:
Enter n value:5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
