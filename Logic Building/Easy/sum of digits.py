# Given a number n, find the sum of its digits.


def sumOfDigits1(x):
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)
    return sum


print(sumOfDigits1(123))
print(sumOfDigits1(345))


def sumOfDigits2(x):
    sum = 0
    while x != 0:
        last = x % 10  # % gives a remainder
        sum += last
        x //= 10  # removes the last digit (divides and rounds the result down to the nearest whole number)
    return sum


print(sumOfDigits2(123))