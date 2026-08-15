#read n
n=int(input("Enter n value:"))
#print centered pyramid
for i in range(n,0,-1):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)
#output:
Enter n value:5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
