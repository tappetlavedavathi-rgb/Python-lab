a=[10,20,30,40,50]
a.append(60)
print("append:",a)
a.insert(5,25)
print("insert:",a)
a.extend([70,80])
print("Extend:",a)
a.remove(30)
print("Remove:",a)
a.pop()
print("pop:",a)
a.sort()
print("sort:",a)
a.reverse()
print("reverse:",a)
a.count(20)
print("count of 20:",a)
a.index(40)
print("index of 40:",a)
#output:
append: [10, 20, 30, 40, 50, 60]
insert: [10, 20, 30, 40, 50, 25, 60]
Extend: [10, 20, 30, 40, 50, 25, 60, 70, 80]
Remove: [10, 20, 40, 50, 25, 60, 70, 80]
pop: [10, 20, 40, 50, 25, 60, 70]
sort: [10, 20, 25, 40, 50, 60, 70]
reverse: [70, 60, 50, 40, 25, 20, 10]
count of 20: [70, 60, 50, 40, 25, 20, 10]
index of 40: [70, 60, 50, 40, 25, 20, 10]

