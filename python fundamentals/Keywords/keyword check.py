# T.vedavathi
# check wether a word is a python keyword or not
import keyword
word=input("Enter a word:")
if keyword.iskeyword(word):
    print(word, "is a python keyword.")
else:
    print(word, "is not a python keyword.")    
