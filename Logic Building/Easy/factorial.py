# Given the non-negative integers n , compute the factorial of a given number.
# Note: Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1, for n = 0, factorial is 1.
# 5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


print(factorial(5))