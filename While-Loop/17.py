# WAJP to print and count all the factors of
# a number.

# i/p: 28
# o/p: 1 2 4 7 14 28
# Total Factors are: 6

i = 1
c = 0

while i <= 28:
    if 28 % i == 0:
        c += 1
        print(i)
    i += 1
print(f"Total Factors are:{c}")
