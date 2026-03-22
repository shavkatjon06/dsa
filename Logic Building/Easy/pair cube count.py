# Given n, count all 'a' and 'b' that satisfy the condition a^3 + b^3 = n.
# Where (a, b) and (b, a) are considered two different pairs


def countPairs(n):
    count = 0
    arr = []
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a**3 + b**3 == n:
                arr.append(f"{a**3} + {b ** 3} = {n}")
                count += 1
    return count, arr


print(countPairs(9))
print(countPairs(28))