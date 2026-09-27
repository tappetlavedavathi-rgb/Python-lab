from functools import reduce
numbers = [2, 3, 4, 5]
# (a) Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)
# (b) Maximum value without using max()
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum:", maximum)
# (c) Concatenate strings into a sentence
words = ["Python", "is", "easy", "to", "learn"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("Sentence:", sentence)
#output:
Product: 120
Maximum: 5
Sentence: Python is easy to learn

