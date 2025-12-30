# WAJP to print and count all the numbers
# from 1 to 100 which are perfect cube.

i = 1
c = 0

while i**3 <= 100:
    print(i**3)
    c += 1
    i += 1
print(c)
