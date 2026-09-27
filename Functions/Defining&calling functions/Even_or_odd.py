def is_even(n):
    return n%2==0
print("Even or odd checking")
for i in range(1,6):
    num=int(input("Enter n value: "))
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
#output:
Even or odd checking
Enter n value: 2
2 is even
Enter n value: 1
1 is odd
Enter n value: 3
3 is odd
Enter n value: 5
5 is odd
Enter n value: 4
4 is even

