def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Ordered Items:")
    for item in items:
        print("-", item)
    print("Discount:", discount, "%")
    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").title() + ":", value)
order_summary("Meera","Laptop","Mouse",discount=10,delivery_address="Hyderabad",gift_wrap=True)
#output:
Customer: Meera
Ordered Items:
- Laptop
- Mouse
Discount: 10 %
Extra Information:
Delivery Address: Hyderabad
Gift Wrap: True

    
