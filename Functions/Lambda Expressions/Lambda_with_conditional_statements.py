# Lambda function to check pass/fail
grade = lambda marks: "Pass" if marks >= 40 else "Fail"
# List of 6 marks
marks_list = [35, 45, 67, 28, 40, 82]
# Print result for each student
for marks in marks_list:
    print(marks, ":", grade(marks))
#output:
35 : Fail
45 : Pass
67 : Pass
28 : Fail
40 : Pass
82 : Pass

