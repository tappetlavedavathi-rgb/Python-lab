def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
# Example
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
#output:
Enter a value:10
Enter b value:5
GCD: 5
LCM: 10

