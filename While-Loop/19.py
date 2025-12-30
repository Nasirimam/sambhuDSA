n = 8
i = 1
c = 0
while i <= n:
    if n % i == 0:
        c += 1
        if c > 3:
            break
    i += 1
print(c == 3)
