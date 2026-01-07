# WAJP to take user input and print and count
# all the factors of the number.

num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Total factors:", count)
