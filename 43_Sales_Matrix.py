# Multi-Branch Sales Matrix Comparison

b = int(input("Enter number of branches: "))
p = int(input("Enter number of products: "))
d = int(input("Enter number of days: "))

if b < 1 or p < 1 or d < 1:
    print("Invalid! Branches, products and days must be at least 1.")
else:
    # build matrix: rows = branches, columns = products
    sales = []
    for i in range(b):
        row = []
        for j in range(p):
            total = 0
            for k in range(d):
                while True:
                    v = int(input("Branch " + str(i + 1) + " Product " + str(j + 1) + " Day " + str(k + 1) + ": "))
                    if v >= 0:
                        break
                    print("Invalid! Sales cannot be negative.")
                total = total + v
            row.append(total)
        sales.append(row)

    print("\n--- Sales Matrix (rows = branches, columns = products) ---")
    for i in range(b):
        print("Branch", i + 1, ":", sales[i])

    # product totals (column-wise)
    print("\n--- Product totals ---")
    for j in range(p):
        col_total = 0
        for i in range(b):
            col_total = col_total + sales[i][j]
        print("Product", j + 1, "Total:", col_total)

    # branch totals (row-wise)
    print("\n--- Branch totals ---")
    branch_totals = []
    for i in range(b):
        t = 0
        for j in range(p):
            t = t + sales[i][j]
        branch_totals.append(t)
        print("Branch", i + 1, "Total:", t)

    # best branch(es)
    highest = max(branch_totals)
    print("\nBest branch(es) with total", highest, ":")
    for i in range(b):
        if branch_totals[i] == highest:
            print("Branch", i + 1)

    # best product in each branch
    print("\n--- Best product in each branch ---")
    for i in range(b):
        best = 0
        for j in range(1, p):
            if sales[i][j] > sales[i][best]:
                best = j
        print("Branch", i + 1, "-> Product", best + 1, "(" + str(sales[i][best]) + ")")