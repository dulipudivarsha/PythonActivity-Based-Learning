# Hollow Diamond Numeric Pattern

n = int(input("Enter size (odd number, minimum 3): "))

if n < 3 or n % 2 == 0:
    print("Invalid size! Enter an odd number that is 3 or more.")
else:
    mid = n // 2

    for i in range(n):
        # distance from the middle row
        if i <= mid:
            d = i
        else:
            d = n - 1 - i

        spaces = mid - d
        number = d + 1

        # leading spaces
        line = " " * spaces

        if d == 0:
            # top and bottom tip
            line = line + str(number)
        else:
            # left number, inner gap, right number
            line = line + str(number) + " " * (2 * d - 1) + str(number)

        print(line)