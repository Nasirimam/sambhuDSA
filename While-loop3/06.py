i = int(input("Enter A number: "))

max = 0
min = 10
while i > 0:
    if (i % 10) > max:
        max = i % 10
    if (i % 10) < min:
        min = i % 10
    i = i // 10
print(max - min)
