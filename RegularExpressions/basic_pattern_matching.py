import re
#task 1
sentence="1024 requests were served in 3 seconds"
m1=re.match(r"\d",sentence)
print("starts with digit:",bool(m1))
m2=re.search(r"served",sentence)
print("position of served:",m2.span())
m3=re.fullmatch(r"\d+","12345")
print("12345:",bool(m3))
m4=re.fullmatch(r"\d+","123a5")
print("123a5:",bool(m4))
#output:
starts with digit: True
position of served: (19, 25)
12345: True
123a5: False
