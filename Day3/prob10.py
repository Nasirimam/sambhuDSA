# Given a character, check if it's uppercase, lowercase, digit or special character.

a = "0"

res = (
    "Uppercase"
    if ("A" <= a <= "Z")
    else (
        "Lowercase"
        if ("a" <= a <= "z")
        else "Digit" if ("0" <= a <= "9") else "Spaical Char"
    )
)
print(res)
