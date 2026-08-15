# Read year, month and day
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
# Check whether the month is valid
if month < 1 or month > 12:
    print("Invalid month")
# Find number of days in the month
else:
#feb has 29 days
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28
# These months have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
# Remaining months have 31 days        
    else:
      days = 31
#Check whether the day is valid
if day >= 1 and day <= days:
     print("Valid date")
else:
    print("Invalid date")
#output:
Enter year: 2024
Enter month: 2
Enter day: 29
Valid date
    
    
