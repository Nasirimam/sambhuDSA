a = 12
b = 43
c = 34
d = 22

max = (
    a
    if (a > b and a > c and a > d)
    else b if (b > c and b > d) else c if (c > d) else d
)

print(max)
