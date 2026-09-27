print("using positonal arguments")
def student(name,rollno,branch):
    print("Name:",name)
    print("rollno:",rollno)
    print("Branch:",branch)
student("vedavathi",54,"CSE")
print("using keyword arguments")
student(name="navya",rollno=52,branch="CSE")
#output:
using positonal arguments
Name: vedavathi
rollno: 54
Branch: CSE
using keyword arguments
Name: navya
rollno: 52
Branch: CSE



