i = int(input("Enter A number: "))
c = 0
while i > 0:
    if (i % 10) % 2 != 0:
        c += 1
    i = i // 10
print(c)
