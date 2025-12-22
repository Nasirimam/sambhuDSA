# WAP to check whether the three sides of a triangle is valid or not.

a = 20
b = 15
c = 6

print(
    "Valid Triangle"
    if a + b > c and b + c > a and c + a > b
    else "Not A Valid Triangle"
)
