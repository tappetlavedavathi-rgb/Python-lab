#read sides
a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
#check whether it is a valid triangle or not
if a+b<c or a+c<=b or b+c<=a:
    print("NOT A VALID TRIANGLE")
#checking for equilateral triangle    
elif a==b and b==c:
    print("EQUILATERAL TRIANGLE")
#checking for isosceles triangle     
elif a==b or b==c or a==c:
    print("ISOSCELES TRIANGLE")
#it is a scalene triangle
else:
    print("SCALENE TRIANGLE")
#output:
Enter side 1:9
Enter side 2:9
Enter side 3:3
ISOSCELES TRIANGLE
    
