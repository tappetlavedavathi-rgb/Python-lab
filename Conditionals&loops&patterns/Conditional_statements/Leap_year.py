#read year
year=int(input("Enter a year:"))
#checking whether a given year is a leap year or not
if (year%400==0) or (year%4==0 and year%100!=0):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
#output:
Enter a year:2024
LEAP YEAR    
    
    
