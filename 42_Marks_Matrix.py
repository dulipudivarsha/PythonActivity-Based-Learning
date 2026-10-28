# Student Marks Matrix Analysis

LOW_AVG = 40

n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

if n < 1 or m < 1:
    print("Invalid! Students and subjects must be at least 1.")
else:
    # build the matrix (nested list)
    marks = []
    for i in range(n):
        row = []
        for j in range(m):
            while True:
                mark = int(input("Enter marks of student " + str(i + 1) + " subject " + str(j + 1) + ": "))
                if mark >= 0 and mark <= 100:
                    break
                print("Invalid! Marks must be between 0 and 100.")
            row.append(mark)
        marks.append(row)

    # row-wise: total and average of each student
    print("\n--- Student-wise ---")
    totals = []
    for i in range(n):
        total = 0
        for j in range(m):
            total = total + marks[i][j]
        totals.append(total)
        print("Student", i + 1, "Total:", total, "Average:", round(total / m, 2))

    # top performer(s)
    highest = max(totals)
    print("\nTop performer(s) with total", highest, ":")
    for i in range(n):
        if totals[i] == highest:
            print("Student", i + 1)

    # column-wise: average and highest of each subject
    print("\n--- Subject-wise ---")
    low_subjects = []
    for j in range(m):
        col_total = 0
        col_high = marks[0][j]
        for i in range(n):
            col_total = col_total + marks[i][j]
            if marks[i][j] > col_high:
                col_high = marks[i][j]
        avg = col_total / n
        print("Subject", j + 1, "Average:", round(avg, 2), "Highest:", col_high)
        if avg < LOW_AVG:
            low_subjects.append(j + 1)

    print("\nSubjects with low average (below 40):")
    if len(low_subjects) == 0:
        print("None")
    else:
        for s in low_subjects:
            print("Subject", s)