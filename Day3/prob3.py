# WAP to check and print the given number is divisible by both 3 and 5 or only by 3,only by 5 or None.

num = 15
print(
    "Divisible By 3 and 5 Both"
    if num % 3 == 0 and num % 5 == 0
    else (
        "Divisible By 3 Only"
        if num % 3 == 0
        else ("Divisible By 5 Only" if num % 5 == 0 else "Not Divisible by 3 or 5")
    )
)

# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible By 3 and 5 Both")
# elif num % 3 == 0:
#     print("Divisible By 3 Only")
# elif num % 5 == 0:
#     print("Divisible By 5 Only")
