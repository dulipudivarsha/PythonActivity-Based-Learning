# Tuple-Based Employee Shift Conflict Detection

n = int(input("Enter number of shifts: "))

if n < 2:
    print("Invalid! Enter at least 2 shifts.")
else:
    # store each shift as a tuple
    shifts = []
    for i in range(n):
        emp = input("Enter employee name: ")
        while True:
            start = int(input("Enter start hour (0-23): "))
            end = int(input("Enter end hour (1-24): "))
            if start >= 0 and end <= 24 and start < end:
                break
            print("Invalid! Start must be less than end, within 0 to 24.")
        shifts.append((emp, start, end))

    print("\n--- Shifts ---")
    for emp, start, end in shifts:        # tuple unpacking
        print(emp, start, "to", end)

    # compare every pair of shifts
    conflicts = []
    for i in range(n):
        for j in range(i + 1, n):
            e1, s1, f1 = shifts[i]
            e2, s2, f2 = shifts[j]
            if e1 == e2 and s1 < f2 and s2 < f1:
                conflicts.append((e1, s1, f1, s2, f2))

    print("\n--- Conflicts ---")
    if len(conflicts) == 0:
        print("None")
    else:
        for e, s1, f1, s2, f2 in conflicts:
            print(e, s1, "to", f1, "conflicts with", s2, "to", f2)