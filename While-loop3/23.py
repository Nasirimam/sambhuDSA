num = 34843
temp = num
l = len(str(num))
out = 0

while num > 0:
    out += (num % 10) * (10 ** (l - 1))
    l -= 1
    num //= 10

print("Palindrom" if out == temp else "Not Palindrome")
