magicNumber = int(input("Enter a number: "))

for m in range(100):
    if m is magicNumber:
        print(m, "is the magic number")
        break
    else:
        print(m)

