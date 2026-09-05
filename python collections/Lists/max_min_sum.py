a=[10,3,4,25,45]
max=a[0]
min=a[0]
total=0
for num in a:
    if num>max:
        max=num
    if num<min:
        min=num
    total+=num
print("Maximum:",max)
print("Minimum:",min)
print("sum:",total)
#output:
Maximum: 45
Minimum: 3
sum: 87
