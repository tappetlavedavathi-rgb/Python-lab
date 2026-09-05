n=int(input("Enter number of items: "))
items = {}
for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    items[name] = price
highest_item = max(items,key=items.get)
lowest_item = min(items,key=items.get)
print("Highest price item:",highest_item, "-",items[highest_item])
print("Lowest price item:",lowest_item, "-",items[lowest_item])
#output:
Enter number of items: 5
Enter item name: fruits
Enter price: 100
Enter item name: flowers
Enter price: 50
Enter item name: chocolates
Enter price: 200
Enter item name: vegetables
Enter price: 150
Enter item name: milk
Enter price: 20
Highest price item: chocolates - 200.0
Lowest price item: milk - 20.0
