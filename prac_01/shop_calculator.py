"""
CP1404/CP5632 - Week 1 Practical - Shop Calculator
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au

Pseudocode:
get number_of_items
for each_item in range(number_of_items):
    get price for each_item
sum price of each item as total_price
if total_price > $100:
    total_price *= 0.9
"""
DISCOUNT_RATE = 0.9

number_of_items = int(input("Number of items: "))
# Error checking while the quantity is negative
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
# Sum up the price of each item
total_price = 0
for i in range(number_of_items):
    price_per_item = input("Price of item: ")
    total_price += float(price_per_item)
# Apply discount if possible
if total_price > 100:
    total_price *= DISCOUNT_RATE
print(f'Total price for {number_of_items} items is ${total_price:.2f}')
