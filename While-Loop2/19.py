# WAJP to accept a input from user and
# print factorial of that number.
# i/p: 6
# o/p: 6!= 720

num = int(input("Enter A Number: "))
i = 1
f = 1

while i <= num:
    f *= i
    i += 1

print("Fact:", f)
