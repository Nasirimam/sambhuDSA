n = 42765
sum = 0
while n > 0:
    if (n % 10) <= 5:
        sum += n % 10
    n //= 10
print(sum)
