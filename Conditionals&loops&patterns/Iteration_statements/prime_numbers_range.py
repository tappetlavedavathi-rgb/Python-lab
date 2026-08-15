# Read the limits
start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))
print("Prime numbers are:")
# Check every number between the limits
for n in range(start, end + 1):
    if n > 1:
        count = 0
        # Check factors of n
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        # Prime number has exactly two factors
        if count == 2:
            print(n, end=" ")
#output:
Enter starting limit: 2
Enter ending limit: 100
Prime numbers are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

            
