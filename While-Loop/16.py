# WAJP to count the factors of a number.

# i/p: 28
# o/p: Total Factors are: 6

i = 1
c = 0

while i <= 28:
    if 28 % i == 0:
        c += 1
    i += 1
print(c)
