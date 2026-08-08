read=4
write=2
permission=read | write
print("Permission value:",permission)
if permission & write:
    print("Write permission is set")
else:
    print("Write permission is not set")
#output:
Permission value: 6
Write permission is set

