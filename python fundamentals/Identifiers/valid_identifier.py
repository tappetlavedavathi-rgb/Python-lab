# Challenge
# Check whether a given name is a valid identifier

import keyword

name = input("Enter an identifier: ")

if (name[0].isalpha() or name[0] == "_") and all(ch.isalnum() or ch == "_" for ch in name) and not keyword.iskeyword(name):
    print("Valid Identifier")
else:
    print("Invalid Identifier")