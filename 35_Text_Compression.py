# Text Compression Using Character Runs

text = input("Enter a string: ")

if len(text) == 0:
    print("Invalid! String cannot be empty.")
else:
    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1
        else:
            encoded = encoded + text[i - 1] + str(count)
            count = 1

    # add the last run
    encoded = encoded + text[len(text) - 1] + str(count)

    print("Original :", text)
    print("Encoded  :", encoded)
    print("Original length:", len(text))
    print("Encoded length :", len(encoded))

    if len(encoded) < len(text):
        print("Compression is beneficial. Saved", len(text) - len(encoded), "characters.")
    else:
        print("Compression is NOT beneficial.")