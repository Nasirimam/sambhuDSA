# WAJP to print and count all the numbers
# from 1 to 1000 which are divisible by 7
# and also ends with 7.

i = 1

while i <= 1000:
    if i % 7 == 0:
        if i % 10 == 7 or i % 100 == 7:
            print(i)
    i += 1
