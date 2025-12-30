# WAJP to print a number is a prime
# number or not.

i = 2
num = 19

while i < num:
    if num % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")
