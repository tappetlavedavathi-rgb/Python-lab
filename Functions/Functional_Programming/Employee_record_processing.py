from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 50000},
    {"name": "Sita", "department": "HR", "salary": 45000},
    {"name": "Amit", "department": "IT", "salary": 60000},
    {"name": "Priya", "department": "Finance", "salary": 55000},
    {"name": "Kiran", "department": "IT", "salary": 52000}
]
# Select employees from the IT department
it_employees = filter(
    lambda emp: emp["department"] == "IT",
    employees
)
# Give selected employees a 10% salary hike
# Create new dictionaries without modifying originals
hiked_employees = map(
    lambda emp: {
        **emp,
        "salary": emp["salary"] * 1.10
    },
    it_employees
)
# Convert map result to a list
hiked_employees = list(hiked_employees)
# Display employees after hike
print("IT Employees after 10% hike:")
for emp in hiked_employees:
    print(emp)
# Calculate total salary expenditure
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)
print("\nTotal salary expenditure:", total_salary)
#output:
IT Employees after 10% hike:
{'name': 'Ravi', 'department': 'IT', 'salary': 55000.00000000001}
{'name': 'Amit', 'department': 'IT', 'salary': 66000.0}
{'name': 'Kiran', 'department': 'IT', 'salary': 57200.00000000001}

Total salary expenditure: 178200.0

