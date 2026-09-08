s = input("Enter a sentence: ")
words = s.split()
result = ""
for word in words:
    result = result + word[0].upper() + word[1:] + " "
print("Title Case:", result)
#output:
Enter a sentence: python is easy
Title Case: Python Is Easy 
