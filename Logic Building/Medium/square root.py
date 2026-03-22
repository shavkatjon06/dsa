# Given a positive integer n, find its square root. If n is not a perfect square,
# then return floor of √n.


def squareRoot(n):
    low = 1
    high = n
    result = 1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


print(squareRoot(11))
print(squareRoot(4))
