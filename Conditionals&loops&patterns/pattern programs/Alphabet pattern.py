#read n
n=int(input("Enter n value:"))
#print alphabet pattern
for i in range(n):
    ch=chr(65+i)
    for j in range(i+1):
        print(ch, end=" ")
    print()
#output:
Enter n value:5
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

