def CheckPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


num = int(input("Enter A Number: "))
c = 0
for i in range(2, num + 1):
    if CheckPrime(i):
        c += 1
print(c)
