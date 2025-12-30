# WAJP to print all the numbers from 1 to
# 100 which are perfect square.

i = 1

while i <= 100:
    print(i**2)
    if i**2 >= 100:
        break
    i += 1
