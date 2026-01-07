num = int(input("Enter The kth Num Prime You Want: "))


def CheckPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


c = 0
i = 2
prime = 0
while c < num:
    if CheckPrime(i):
        prime = i
        c += 1
    i += 1
else:
    print(prime)
