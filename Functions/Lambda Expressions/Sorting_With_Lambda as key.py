# List of tuples: (student_name, marks)
students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]
# Sort by marks in descending order
sorted_students = sorted(
    students,
    key=lambda s: s[1],
    reverse=True
)
print("Students sorted by marks:")
for student in sorted_students:
    print(student)
# List of strings
words = ["Python", "AI", "Programming", "Code", "Lambda"]
# Sort strings by their length
sorted_words = sorted(words, key=lambda word: len(word))
print("\nStrings sorted by length:")
print(sorted_words)
#output:
Students sorted by marks:
('Sita', 92)
('Ravi', 78)
('Amit', 65)

Strings sorted by length:
['AI', 'Code', 'Python', 'Lambda', 'Programming']

