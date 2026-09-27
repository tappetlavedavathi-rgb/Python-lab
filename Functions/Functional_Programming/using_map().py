# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
temperatures = [0, 10, 20, 30, 40]
fahrenheit = list(map(celsius_to_fahrenheit, temperatures))
print("Celsius temperatures:", temperatures)
print("Fahrenheit temperatures:", fahrenheit)
# Convert strings to uppercase
def to_uppercase(text):
    return text.upper()
words = ["hello", "python", "programming", "world"]
uppercase_words = list(map(to_uppercase, words))
print("Original words:", words)
print("Uppercase words:", uppercase_words)
#output:
Celsius temperatures: [0, 10, 20, 30, 40]
Fahrenheit temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]
Original words: ['hello', 'python', 'programming', 'world']
Uppercase words: ['HELLO', 'PYTHON', 'PROGRAMMING', 'WORLD']

