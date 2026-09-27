def power(base, exp):
    #Zero
    if exp == 0:
        return 1
    # Negative exponent
    if exp < 0:
        return 1 / power(base, -exp)
    # Positive exponent
    return base * power(base, exp - 1)
# Examples
print("2^5 =", power(2, 5))
print("5^0 =", power(5, 0))
print("2^-3 =", power(2, -3))
#output:
2^5 = 32
5^0 = 1
2^-3 = 0.125

