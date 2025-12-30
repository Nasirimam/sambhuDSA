n = 43705

temp = n
c = 0

while temp > 0:
    c += 1
    temp //= 10

div = 10 ** (c - 1)

while div > 0:
    print(n // div)
    n = n % div
    div //= 10
