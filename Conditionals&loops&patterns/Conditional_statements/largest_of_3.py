#read numbers
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
c=int(input("Enter third no:"))
#find the largest no usind nested if
if a>b:
    if a>c:
        print("largest=", a)
    else:
        print("largest=", c)
else:
    if b>c:
        print("largest=", b)
    else:
        print("largest=", c)
#output:
Enter first no:5
Enter second no:4
Enter third no:3
largest= 5        
