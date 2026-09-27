def simple_intrest(p,t,r):
#return the simple intrest using formula
    return (p*t*r)/100;
print("Simple intrest")
#entering the users input values
p=float(input("Enter p value:"))
t=float(input("Enter t value:"))
r=float(input("Enter r value:"))
#calling the function
SI=simple_intrest(p,t,r);
print("simple intrset is:",SI)
#output:
Simple intrest
Enter p value:100
Enter t value:50
Enter r value:20
simple intrset is: 1000.0

