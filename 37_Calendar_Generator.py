# Nested Loop Calendar Generator

start = int(input("Enter starting weekday (1=Mon ... 7=Sun): "))
days = int(input("Enter number of days (28 to 31): "))

if start < 1 or start > 7:
    print("Invalid starting weekday!")
elif days < 28 or days > 31:
    print("Invalid number of days!")
else:
    print("Mon Tue Wed Thu Fri Sat Sun")
    day = 1

    for week in range(6):
        # stop if all days are already printed
        if day > days:
            break

        line = ""
        for col in range(1, 8):
            # blank before the 1st day, or after the last day
            if (week == 0 and col < start) or day > days:
                line = line + "    "
            else:
                line = line + str(day).rjust(3) + " "
                day = day + 1
        print(line)
        