# For the given three numbers. Swap 1st into 2nd nd into 3rd and 3rd into 1st number.
# a. Without using fourth variable

a = -10
b = 20
c = 30

a = a + b + c

b = a - (b + c)
c = a - (b + c)
a = a - (b + c)

print(a)
print(b)
print(c)
