# You are given two positive integers n and k.
# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order,
# return the kth factor in this list or return -1 if n has less than k factors.


def kthFactor(n, k):
    i = 1
    c = []
    while i <= n:
        if n % i == 0:
            c.append(i)
        i += 1
    return c[k - 1] if k <= len(c) else -1


print(kthFactor(12, 3))
