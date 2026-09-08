s = input("Enter a string: ")
if s.isdigit():
    print("Only digits")
elif s.isalpha():
    print("Only alphabets")
elif s.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters")
#output:
Enter a string: vedavathi28
Alphanumeric
