#read a character
ch=input("Enter a character:")
#check whether it is a vowel
if ch in "aeiouAEIOU":
    print("it is a VOWEL")
#check whether it is a consonant
elif ch.isalpha():
    print("it is a CONSONANT")
#check whether it is a digit
elif ch.isdigit():
    print("it is a DIGIT")
#special symbols    
else:
    print("special symbol")
#output:
Enter a character:a
it is a VOWEL
    
