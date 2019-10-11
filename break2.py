available = 5
x = int(input("Enter a value that you want: "))

i = 1
while i <= x:
    if x > available:
        print("Stock is Over")
        break
    print("success")
    i += 1

