str = "eeeeee"
l = len(str) - 1
i = 0

while i < l:
    if str[i] != str[l]:
        print("Not Pal")
        break
    i += 1
    l -= 1
else:
    print("pal")
