# WAJP to count all the numbers from 1 to
# 100 which are divisible by 7.

i = 1
c = 0

while i <= 100:
    if i % 7 == 0:
        c += 1
    i += 1

print(f"Total Count - {c}")
