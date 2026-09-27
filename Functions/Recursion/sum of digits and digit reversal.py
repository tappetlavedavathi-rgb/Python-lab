def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)
def reverse_number(n):
    def reverse_helper(n, reversed_num):
        if n == 0:
            return reversed_num

        return reverse_helper(
            n // 10,
            reversed_num * 10 + n % 10
        )

    return reverse_helper(n, 0)
number = int(input("enter a number:"))
print("Number:", number)
print("Sum of digits:", sum_of_digits(number))
print("Reversed number:", reverse_number(number))
#output:
enter a number:123
Number: 123
Sum of digits: 6
Reversed number: 321

