n = 3745
l = len(str(n))
out = 0

while n > 0:
    out += (n % 10) * (10 ** (l - 1))
    n //= 10
    l -= 1
print(out)
