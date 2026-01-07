# WAJP to take user input and print whether the
# number is Prime number or not.

num = int(input("Enter A Num: "))

for i in range(2, num):
    if num % i == 0:
        print("Not A Prime")
        break
else:
    print("Prime Number")
