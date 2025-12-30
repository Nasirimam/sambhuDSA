def commonFactors(self, a: int, b: int) -> int:
    i = 1
    c = 0
    while i <= a or i <= b:
        if a % i == 0 and b % i == 0:
            c += 1
        i += 1
    return c


print(commonFactors(0, 12, 6))
