# Retail Billing with Multiple Discount Rules

MAX_DISCOUNT = 500

n = int(input("Enter number of products: "))
names = []
qtys = []
prices = []
amounts = []
taxes = []

for i in range(n):
    name = input("Enter product name: ")

    # input validation
    while True:
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        cat = input("Enter category (G/C/E): ").upper()
        if price > 0 and qty > 0 and cat in ["G", "C", "E"]:
            break
        print("Invalid! Price, quantity must be positive and category must be G, C or E.")

    # category-wise tax rate
    if cat == "G":
        rate = 0.05
    elif cat == "C":
        rate = 0.12
    else:
        rate = 0.18

    amount = price * qty
    tax = amount * rate

    names.append(name)
    qtys.append(qty)
    prices.append(price)
    amounts.append(amount)
    taxes.append(tax)

subtotal = sum(amounts)
total_tax = sum(taxes)

# threshold discount
if subtotal > 5000:
    discount = subtotal * 0.10
elif subtotal > 2000:
    discount = subtotal * 0.05
else:
    discount = 0

# maximum concession limit
capped = False
if discount > MAX_DISCOUNT:
    discount = MAX_DISCOUNT
    capped = True

final_bill = subtotal - discount + total_tax

# itemized invoice
print("\n----- INVOICE -----")
print("Item   Qty   Price   Amount   Tax")
for i in range(n):
    print(names[i], "  ", qtys[i], "  ", prices[i], "  ", round(amounts[i], 2), "  ", round(taxes[i], 2))
print("-------------------")
print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
if capped:
    print("(Discount capped at Rs 500)")
print("Total Tax:", round(total_tax, 2))
print("Final Bill:", round(final_bill, 2))