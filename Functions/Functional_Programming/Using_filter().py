# 1. Extract prime numbers from 1 to 50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = list(range(1, 51))
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)
# 2. Extract palindromes from a list of words
words = ["madam", "hello", "level", "python", "radar", "world", "civic"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print("Palindromes:", palindromes)
#output:
Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Palindromes: ['madam', 'level', 'radar', 'civic']

