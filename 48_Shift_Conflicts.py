# Tuple-Based Product Catalogue Audit

REORDER_LEVEL = 10

n = int(input("Enter number of products: "))

if n < 1:
    print("Invalid! Number of products must be at least 1.")
else:
    # store each product as a tuple
    catalogue = []
    for i in range(n):
        pid = input("Enter product id: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        catalogue.append((pid, price, stock))

    # separate valid and invalid records
    valid = []
    invalid = []
    for item in catalogue:
        pid, price, stock = item          # tuple unpacking
        if price <= 0 or stock < 0:
            invalid.append(item)
        else:
            valid.append(item)

    # inventory value of valid records
    print("\n--- Valid products ---")
    total_value = 0
    for pid, price, stock in valid:
        value = price * stock
        total_value = total_value + value
        print(pid, "Price:", price, "Stock:", stock, "Value:", value)
    print("Total inventory value:", total_value)

    # invalid records
    print("\n--- Invalid records ---")
    if len(invalid) == 0:
        print("None")
    else:
        for pid, price, stock in invalid:
            print(pid, "Price:", price, "Stock:", stock)

    # replenishment
    print("\n--- Items needing replenishment (stock below 10) ---")
    need = False
    for pid, price, stock in valid:
        if stock < REORDER_LEVEL:
            print(pid, "Stock:", stock, "Order at least:", REORDER_LEVEL - stock)
            need = True
    if not need:
        print("None")