# Read a number
n = int(input("Enter a number: "))
count = 0
# Check divisibility
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
# A prime number has exactly two factors
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
#output:
Enter a number: 2
Prime number
