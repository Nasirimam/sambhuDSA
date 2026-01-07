def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


num = int(input("Enter A Num: "))
c = 0
for i in range(2, num + 1):
    if checkPrime(i):
        sum = 0
        for j in str(i):
            sum += int(j)
        if checkPrime(sum):
            print(i)
            c += 1
print("Count: ", c)
