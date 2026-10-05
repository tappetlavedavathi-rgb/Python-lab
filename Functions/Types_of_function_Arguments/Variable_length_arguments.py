def total_marks(*numbers):
    total = 0
    for num in numbers:
        total +=num
    avg=total/len(numbers)
    print("sum:",total)
    print("avg:",avg)
total_marks(40, 60, 90)
total_marks(60, 70, 80, 66, 90)
total_marks(90)
#output:
sum: 190
avg: 63.333333333333336
sum: 366
avg: 73.2
sum: 90
avg: 90.0



