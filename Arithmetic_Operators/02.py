# print all number in new line from the start to end
a = 72342
n = len(str(a))
while n > 0:
    temp = n - 1
    print((a // 10**temp) % 10)
    n -= 1
