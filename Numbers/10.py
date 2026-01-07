num = int(input("Enter A Num: "))

temp = num

ans = 0
while num > 0:
    ans *= 10
    ans += num % 10
    num //= 10

print("pal" if ans == temp else "Not Pal")
