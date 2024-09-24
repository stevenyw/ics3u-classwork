store = "No Frills"
item = "Apples"
price = 0.55
quantity = 8
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

print(f"At {store} I bought some {item}.")
print("They sold for $" + str(price) + " each.")
print("I wanted to purchase {} of them.".format(quantity))
print(f"If the subtotal would be ${subtotal}, and the tax is ${round(tax, 3)}, then that'll mean...")
print(f"The total price, with tax included, was ${total}.")

# Its missing the f" string.
# The first one uses f-string, the second one uses concatenation, and the third one uses .format.

# I changed the price from 0.5 to 0.55. This changes the calculations which made the total price, tax & subtotal change.
# I then also changed the quantity from 7 to 8, which resulted in a change in the subtotal, the tax & the total price.
