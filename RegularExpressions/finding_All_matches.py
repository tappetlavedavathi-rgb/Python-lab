import re;
paragraph = "NASA and USA work with ISRO. Python is useful for programming students."
# Capital letters words
capital_words = re.findall(r"\b[A-Z]{2,}\b", paragraph)
print("Capital words:", capital_words)
# Words longer than 6 characters
print("Words longer than 6 characters:")
for match in re.finditer(r"\b[A-Za-z]{7,}\b", paragraph):
    print(match.group(), match.start())
# Dollar amounts
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", amounts)
# Count
print("Number of prices:", len(amounts))
#output:
Capital words: ['NASA', 'USA', 'ISRO']
Words longer than 6 characters:
programming 50
students 62
Dollar amounts: ['$3.50', '$1.20', '$4.75']
Number of prices: 3


