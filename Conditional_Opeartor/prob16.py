# Given three numbers, print them in sorted order (ascending)
a = 13
b = 35
c = 53

first = a if (a < b and a < c) else b if (b < c) else c
last = a if (a > b and a > c) else b if (b > c) else c
mid = a + b + c - (first + last)


print(first, mid, last)
