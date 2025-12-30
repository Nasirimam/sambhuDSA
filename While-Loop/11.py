# WAJP to print and count all the numbers
# from 1 to 100 which are perfect square.

i = 1
c = 0

while i * i <= 100:
    print(i * i)
    c += 1
    i += 1
print(c)
