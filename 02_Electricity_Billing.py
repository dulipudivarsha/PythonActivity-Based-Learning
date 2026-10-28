# Progressive Electricity Billing

FIXED_CHARGE = 50

n = int(input("Enter number of months: "))
units_list = []
bills_list = []

for i in range(n):
    # input validation
    while True:
        units = int(input("Enter units for month " + str(i + 1) + ": "))
        if units >= 0:
            break
        print("Invalid! Units cannot be negative.")

    # slab calculation
    if units <= 100:
        energy = units * 3
    elif units <= 200:
        energy = 100 * 3 + (units - 100) * 5
    else:
        energy = 100 * 3 + 100 * 5 + (units - 200) * 8

    # surcharge and rebate
    surcharge = 0
    rebate = 0
    if units > 300:
        surcharge = 0.10 * energy
    if units < 50:
        rebate = 0.05 * energy

    # final bill
    bill = energy + surcharge - rebate + FIXED_CHARGE

    units_list.append(units)
    bills_list.append(bill)

# summary
print("\nMonth  Units  Bill")
for i in range(n):
    print(i + 1, "     ", units_list[i], "   ", round(bills_list[i], 2))

# unusual increase check (40% or more)
print("\nUnusual increases:")
found = False
for i in range(1, n):
    increase = (bills_list[i] - bills_list[i - 1]) / bills_list[i - 1] * 100
    if increase >= 40:
        print("Month", i + 1, "increased by", round(increase, 2), "%")
        found = True
if not found:
    print("None")