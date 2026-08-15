#read n
n=int(input("Enter n value:"))
#print increasing numbers in each row
for i in range(1,n+1):
    #increasing part
    for j in range(1,i+1):
        print(j, end=" ")
    #decreasing part
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()
#output:
Enter n value:5
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

