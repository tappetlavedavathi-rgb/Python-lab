#read n
n=int(input("Enter n value:"))
#print centered pyramid
#upper half of dia,ond
for i in range(1,n+1):
    spaces=" "*(n-i)
    stars="* "*(2*i-1)
    print(spaces+stars)
for i in range(n-1,0,-1):
    spaces=" "*(n-i)
    stars="* "*(2*i-1)
    print(spaces+stars)
#output:
Enter n value:4
   * 
  * * * 
 * * * * * 
* * * * * * * 
 * * * * * 
  * * * 
   * 

