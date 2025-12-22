# print second largest of three distinct numbers using ternary operator only.
a = 10
b = 20
c = 15

res = (
    a
    if (a > b and a < c) or (a > c and a < b)
    else b if (b > a and b < c) or (b > c and b < a) else c
)


print(res)
