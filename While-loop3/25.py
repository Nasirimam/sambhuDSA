str = "madam"
i = len(str) - 1
out = ""
while i >= 0:
    out += str[i]
    i -= 1
print("Pal" if out == str else "Not Pal")
