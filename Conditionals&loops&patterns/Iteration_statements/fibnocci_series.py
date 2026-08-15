#read n
n=int(input("Enter no of terms:"))
a=0
b=1
i=1
#print fibnocci series
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1
#output:
Enter no of terms:10
0
1
1
2
3
5
8
13
21
34

