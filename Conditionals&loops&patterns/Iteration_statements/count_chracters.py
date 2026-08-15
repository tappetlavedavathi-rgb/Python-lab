# Read a string
text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
# Check each character
for ch in text:
    if ch in "aeiouAEIOU":
        vowels += 1

    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
# Display the counts
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
#output:
Enter a string: vedavathi@28
Vowels = 4
Consonants = 5
Digits = 2
Spaces = 0
