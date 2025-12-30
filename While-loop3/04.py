i = int(input("Enter A number: "))

while i > 0:
    if (i % 10) >= 5:
        print(i % 10)
    i = i // 10
