# WAJP to print and count all the numbers
# from 1 to 100 which are divisible by 7 or
# ends with 7.

i = 1

while i <= 100:
    if i % 7 == 0 and i % 10 == 7:
        print(i)
    i += 1
