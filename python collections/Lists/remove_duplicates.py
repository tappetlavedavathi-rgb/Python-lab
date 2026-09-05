a=[1,2,3,4,5,6,2,3,5,7]
result=[]
for item in a:
    if item not in result:
        result.append(item)
print(result)
#output:
[1, 2, 3, 4, 5, 6, 7]
