# Read a number
n = int(input("Enter a number: "))
temp = n
sum_digits = 0
count = 0
# Find sum and count of digits
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10
# Find average
average = sum_digits / count
print("Sum =", sum_digits)
print("Average =", average)
#output:
Enter a number: 10
Sum = 1
Average = 0.5
