#read n
n=int(input("Enter n value:"))
#print centered pyramid
for i in range(1,n+1):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)
#output:
Enter n value:5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
