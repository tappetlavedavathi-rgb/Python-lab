def factorial(n):
    if n<0:
        raise ValueError("only positive value")
    if n==0:
        return 1;
    return n*factorial(n-1)
print(factorial(5))
#output:
print(factorial(-5))
File "C:/python folder/Functions/New folder (3)/lab3.1.py", line 3, in factorial
raise ValueError("only positive value")
ValueError: only positive value
print(factorial(5))
120




                
