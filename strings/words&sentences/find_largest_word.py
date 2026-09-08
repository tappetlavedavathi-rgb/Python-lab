s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)
#output:
Enter a sentence: my name is vedavathi
Longest word: vedavathi
