s=input("Enter a string:");
consonants=0;
vowels=0;
digits=0;
spaces=0;
for ch in s:
    if ch in "aeiouAeiou":
        vowels+=1;
    elif ch.isalpha():
        consonants+=1;
    elif ch.isdigit():
        digits+=1;
    elif ch==" ":
        spaces+=1;
print("Voewls=",vowels)
print("Consonants=", consonants)
print("Digits=",digits)
print("Spaces=",spaces)
#output:
Enter a string: vedavathi @28
Voewls= 4
Consonants= 5
Digits= 2
Spaces= 2


        
