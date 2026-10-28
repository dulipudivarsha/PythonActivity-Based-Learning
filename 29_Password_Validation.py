# Password Policy Validation Engine

SPECIALS = "!@#$%&*"
BANNED = ["password", "1234", "qwerty"]

pwd = input("Enter password: ")
errors = []

# rule 1: length
if len(pwd) < 8:
    errors.append("Length must be at least 8")

# rule 2: character categories
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in pwd:
    if ch >= "A" and ch <= "Z":
        has_upper = True
    elif ch >= "a" and ch <= "z":
        has_lower = True
    elif ch >= "0" and ch <= "9":
        has_digit = True
    elif ch in SPECIALS:
        has_special = True

if not has_upper:
    errors.append("Must contain an uppercase letter")
if not has_lower:
    errors.append("Must contain a lowercase letter")
if not has_digit:
    errors.append("Must contain a digit")
if not has_special:
    errors.append("Must contain a special character (!@#$%&*)")

# rule 3: same character 3 times in a row
repeat = False
for i in range(len(pwd) - 2):
    if pwd[i] == pwd[i + 1] and pwd[i + 1] == pwd[i + 2]:
        repeat = True
if repeat:
    errors.append("No character should repeat 3 times in a row")

# rule 4: prohibited words
lower_pwd = pwd.lower()
for word in BANNED:
    if word in lower_pwd:
        errors.append("Contains prohibited word: " + word)

# result
if len(errors) == 0:
    print("Password is VALID")
else:
    print("Password is INVALID")
    print("Reasons:")
    for e in errors:
        print("-", e)