# Given a positive integer n, we have to find the sum of squares of first n natural numbers.

def sumOfSquares(number):
    if number <= 0:
        return "Enter a valid number"
    sum = 0
    for i in range(1, number+1):
        sum += i ** 2
    return sum


print(sumOfSquares(2))
print(sumOfSquares(3))