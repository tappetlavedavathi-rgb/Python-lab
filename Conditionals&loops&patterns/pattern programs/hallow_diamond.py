# Read N
n = int(input("Enter N: "))
# Upper half
for i in range(n):
    spaces = " " * (n - i - 1)
    if i == 0:
        print(spaces + "*")
    else:
        inside = " " * (2 * i - 1)
        print(spaces + "*" + inside + "*")
# Lower half
for i in range(n - 2, -1, -1):
    spaces = " " * (n - i - 1)
    if i == 0:
        print(spaces + "*")
    else:
        inside = " " * (2 * i - 1)
        print(spaces + "*" + inside + "*")
#output:
Enter N: 4
   *
  * *
 *   *
*     *
 *   *
  * *
   *

