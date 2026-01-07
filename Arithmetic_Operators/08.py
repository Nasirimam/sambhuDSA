# Find the Last Digit of a Number Without using % operator.
def last_digit(n):
    return n - (n // 10) * 10


print(last_digit(7334))
