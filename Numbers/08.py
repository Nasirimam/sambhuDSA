def CheckPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


num = int(input("Enter A Number: "))
temp = 0
c = 0
for i in range(2, num + 1):
    if CheckPrime(i):
        if temp % 2 != 0:
            print(i)
        temp += 1
