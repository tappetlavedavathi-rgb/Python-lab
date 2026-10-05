def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price
# (a) Call with only the price
price1 = calculate_price(1000)
print("Price with default tax and discount:", price1)
# (b) Call with price and custom tax_rate
price2 = calculate_price(1000, 10)
print("Price with custom tax rate:", price2)
# (c) Call with all three arguments overridden
price3 = calculate_price(1000, 12, 100)
print("Price with custom tax rate and discount:", price3)
#output:
Price with default tax and discount: 1180.0
Price with custom tax rate: 1100.0
Price with custom tax rate and discount: 1020.0

