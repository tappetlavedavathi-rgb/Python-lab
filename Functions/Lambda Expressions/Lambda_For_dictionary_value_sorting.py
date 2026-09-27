items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}
# Sort dictionary items by price
sorted_items = sorted(
    items.items(),
    key=lambda item: item[1]
)
print("Items from cheapest to most expensive:")
for item, price in sorted_items:
    print(item, ":", price)
#output:
Items from cheapest to most expensive:
Mouse : 800
Keyboard : 1500
Headphones : 2500
Monitor : 12000
Laptop : 55000

